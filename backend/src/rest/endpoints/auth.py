from copy import deepcopy
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from ...common.constants import (HELPSEEKER_TABLE_NAME,
                                 INTERNAL_SERVER_STATUS_CODE, NOT_FOUND,
                                 SUCCESS_STATUS_CODE, CATEGORY_TABLE_NAME, ORGANIZATION_TABLE_NAME, WORKFLOW_TABLE_NAME)
from ...common.dynamodb_connector import DynamoDBConnector
from ...common.helper import Helper
from ...rest.schemas.schema import AuthDetails, HelpSeeker, UserData, HelpSeekerResponse, Category, Organization
from typing import List

router = APIRouter(
    responses={NOT_FOUND: {"description": "Not found"}},
)


@router.post("/login")
def login(auth_details: AuthDetails) -> JSONResponse:
    """authenticate user from the dyanamoDB table"""
    dynamodb = DynamoDBConnector()
    response = dynamodb.authenticate_user(
        username=auth_details.username, password=auth_details.password
    )
    if response:
        Helper.print_message(f"Successfully logged-in for username: {auth_details.username}")
        return JSONResponse(
            content=response.model_dump(),
            status_code=SUCCESS_STATUS_CODE,
            media_type="application/json",
        )
    Helper.print_message("Invalid username and/or password", level="error")
    raise HTTPException(status_code=401, detail="Invalid username and/or password")


@router.get("/last_helpseeker_id")
def get_last_helpseeker_id():
    dynamodb = DynamoDBConnector()
    data = dynamodb.get_last_id_from_dynamodb_table(table_name=HELPSEEKER_TABLE_NAME)
    Helper.print_message(f"last helpseeker id: {data}")
    return JSONResponse(
        content={"last_helpseeker_id": data},
        status_code=SUCCESS_STATUS_CODE,
        media_type="application/json",
    )


@router.post("/register")
def register_help_seeker(user_data: UserData):
    """Register HelpSeeker information"""
    dynamodb = DynamoDBConnector()
    help_seeker: HelpSeeker = user_data.help_seeker
    status_code, help_seeker_response = dynamodb.add_entry_in_helpseeker(help_seeker)
    if status_code == SUCCESS_STATUS_CODE:
        Helper.print_message("successfully added entry in the helpseeker table")
        # add entry in the workflow table
        workflow_data_list = []
        workflow_data = {"helpseeker_id": help_seeker_response.get("id")}
        for enrolled_cat in user_data.enrolled_categories:
            workflow_data["category_id"] = enrolled_cat.category_id
            workflow_data["organization_id"] = enrolled_cat.organization_id
            workflow_data["notes"] = enrolled_cat.notes
            workflow_data["status"] = enrolled_cat.status
            workflow_data["status_enrolled_date"] = enrolled_cat.status_enrolled_date
            workflow_data_list.append(workflow_data)
        status_code = dynamodb.add_entry_in_workflow(workflow_data_list)
        if status_code == SUCCESS_STATUS_CODE:
            Helper.print_message("successfully added entry in the workflow table")
            return JSONResponse(
                content={"message": "registration completed successfully"},
                status_code=SUCCESS_STATUS_CODE,
                media_type="application/json",
            )
    Helper.print_message("Unable to register helpseeker", level="error")
    raise HTTPException(
        status_code=INTERNAL_SERVER_STATUS_CODE, detail="Unable to register helpseeker"
    )


@router.get("/list_helpseekers/{navigator_id}")
def get_all_navigators_from_helpseeker_id(navigator_id: int):
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

    # get data from helpseeker table
    final_response = []
    entries = dynamodb.get_all_items_from_table(HELPSEEKER_TABLE_NAME)
    for entry in entries:
        if navigator_id == int(entry.get("navigator_id")):
            final_response.append(HelpSeekerResponse(**entry).model_dump())

    # get data from workflow table
    entries = dynamodb.get_all_items_from_table(WORKFLOW_TABLE_NAME)
    final_output = []
    for helpseeker_entry in final_response:
        for entry in entries:
            if int(helpseeker_entry["id"]) == int(entry["helpseeker_id"]):
                data = deepcopy(helpseeker_entry)
                category_id = int(entry.get("category_id"))
                organization_id = int(entry.get("organization_id"))
                data["category_id"] = category_id
                data["notes"] = entry.get("notes")
                data["organization_id"] = organization_id
                data["status"] = entry.get("status")
                data["status_enrolled_date"] = entry.get("status_enrolled_date")
                data["category"] = categories_data[category_id]
                data["organization"] = organizations_data[organization_id]
                final_output.append(data)

    Helper.print_message(f"successfully fetched helpseekrs entries based on the navigator_id: {navigator_id}")
    return JSONResponse(
        content=final_output,
        status_code=SUCCESS_STATUS_CODE,
        media_type="application/json",
    )
