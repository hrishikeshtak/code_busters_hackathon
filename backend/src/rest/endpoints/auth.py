from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse

from ...rest.schemas.auth_details import AuthDetails
from ...common.dynamodb_connector import DynamoDBConnector

router = APIRouter(
    # prefix="/auth",
    # tags=["auth"],
    responses={404: {"description": "Not found"}},
    # dependencies=auth_dependencies,
    # include_in_schema=include_in_schema_override,
)


@router.post("/login")
def login(auth_details: AuthDetails) -> JSONResponse:
    """authenticate user from the dyanamoDB table"""
    dynamodb = DynamoDBConnector()
    response = dynamodb.authenticate_user(
        username=auth_details.username, password=auth_details.password
    )
    if response:
        return JSONResponse(
            content=response.model_dump(),
            status_code=200,
            media_type="application/json",
        )
    raise HTTPException(status_code=401, detail="Invalid username and/or password")
