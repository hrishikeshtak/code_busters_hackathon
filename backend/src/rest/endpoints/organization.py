"""rest endpoint for organization"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from ...common.constants import (INTERNAL_SERVER_STATUS_CODE, NOT_FOUND,
                                 ORGANIZATION_TABLE_NAME, SUCCESS_STATUS_CODE)
from ...common.dynamodb_connector import DynamoDBConnector
from ...common.helper import Helper
from ...rest.schemas.schema import Organization

router = APIRouter(
    responses={NOT_FOUND: {"description": "Not found"}},
)


@router.get("/organization")
def get_all_organization():
    """Return all entry from the organization table"""
    dynamodb = DynamoDBConnector()
    response = dynamodb.get_all_items_from_table(ORGANIZATION_TABLE_NAME)
    if response:
        entries = []
        for entry in response:
            entries.append(Organization(**entry).model_dump())
        Helper.print_message("Successfully retrieved organization details from db")
        return JSONResponse(
            content=entries,
            status_code=SUCCESS_STATUS_CODE,
            media_type="application/json",
        )
    Helper.print_message(
        "Unable to retrieves organization details from db", level="error"
    )
    raise HTTPException(
        status_code=INTERNAL_SERVER_STATUS_CODE,
        detail="Unable to retrieves organization details from db",
    )
