"""rest endpoint for category"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from ...common.constants import (CATEGORY_TABLE_NAME, NOT_FOUND,
                                 SUCCESS_STATUS_CODE)
from ...common.dynamodb_connector import DynamoDBConnector
from ...common.helper import Helper
from ...rest.schemas.schema import Category

router = APIRouter(
    responses={NOT_FOUND: {"description": "Not found"}},
)


@router.get("/category")
def get_all_category():
    """Return all entry from the Category table"""
    dynamodb = DynamoDBConnector()
    response = dynamodb.get_all_items_from_table(CATEGORY_TABLE_NAME)
    if response:
        entries = []
        for entry in response:
            entries.append(Category(**entry).model_dump())
        Helper.print_message("Successfully retrieved category details from db")
        return JSONResponse(
            content=entries,
            status_code=SUCCESS_STATUS_CODE,
            media_type="application/json",
        )
    Helper.print_message("Unable to retrieves category details from db", level="error")
    raise HTTPException(
        status_code=NOT_FOUND,
        detail="Unable to retrieves category from db",
    )