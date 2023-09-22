"""rest endpoint for stats"""

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from collections import Counter

from ...common.constants import (
    NOT_FOUND,
    SUCCESS_STATUS_CODE,
    WORKFLOW_TABLE_NAME,
    HELPSEEKER_TABLE_NAME, CATEGORY_TABLE_NAME, ORGANIZATION_TABLE_NAME, NAVIGATOR_TABLE_NAME,
)
from ...common.dynamodb_connector import DynamoDBConnector
from ...rest.schemas.schema import Category, Organization
from ...rest.schemas.schema import WorkflowResponse, HelpSeekerResponse

router = APIRouter(
    responses={NOT_FOUND: {"description": "Not found"}},
)


@router.get("/stats")
def get_stats():
    """Return all stats entry from the workflow table"""
    dynamodb = DynamoDBConnector()
    # fetch all category from dynamodb table
    response = dynamodb.get_all_items_from_table(CATEGORY_TABLE_NAME)
    categories_data = {}
    if response:
        for entry in response:
            data = Category(**entry).model_dump()
            categories_data[data["id"]] = data

    # fetch all organization details from dynamodb table
    response = dynamodb.get_all_items_from_table(ORGANIZATION_TABLE_NAME)
    organizations_data = {}
    if response:
        for entry in response:
            data = Organization(**entry).model_dump()
            organizations_data[data["id"]] = data

    workflow_response = dynamodb.get_all_items_from_table(WORKFLOW_TABLE_NAME)
    final_response = []
    # get helpseeker_id for each category_id
    category_stats = Counter()
    organization_stats = Counter()
    status_stats = Counter()
    navigator_stats = Counter()
    for entry in workflow_response:
        data = WorkflowResponse(**entry).model_dump()
        category_stats[categories_data[data["category_id"]]["name"]] += 1
        organization_stats[organizations_data[data["organization_id"]]["name"]] += 1
        status_stats[data["status"]] += 1
    final_response.append({"category_stats": category_stats})
    final_response.append({"organization_stats": organization_stats})
    final_response.append({"status_stats": status_stats})

    navigator_entries = dynamodb.get_all_items_from_table(NAVIGATOR_TABLE_NAME)
    navigator_details = {}
    for entry in navigator_entries:
        navigator_details[int(entry["id"])] = entry

    entries = dynamodb.get_all_items_from_table(HELPSEEKER_TABLE_NAME)
    for entry in entries:
        data = HelpSeekerResponse(**entry).model_dump()
        navigator_stats[navigator_details[data["navigator_id"]]["username"]] += 1
    final_response.append({"navigator_stats": navigator_stats})
    return JSONResponse(
        content=final_response,
        status_code=SUCCESS_STATUS_CODE,
        media_type="application/json",
    )
