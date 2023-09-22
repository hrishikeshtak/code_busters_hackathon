from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse

from ...rest.schemas.auth_details import AuthDetails, HelpSeeker
from ...common.dynamodb_connector import DynamoDBConnector
from ...common.helper import SUCCESS_STATUS_CODE, INTERNAL_SERVER_STATUS_CODE

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


@router.get("/helpseeker_count")
def get_last_helpseeker_id():
    dynamodb = DynamoDBConnector()
    data = dynamodb.get_last_helpseeker_id()
    print(f"data: {data}")
    return JSONResponse(
        content={"last_helpseeker_id": int(data)},
        status_code=200,
        media_type="application/json",
    )


@router.post("/register")
def register_help_seeker(help_seeker: HelpSeeker):
    """Register HelpSeeker information"""
    dynamodb = DynamoDBConnector()
    status_code = dynamodb.add_entry_in_helpseeker()
    if status_code == SUCCESS_STATUS_CODE:
        return JSONResponse(
            content={"message": "registration completed successfully"},
            status_code=SUCCESS_STATUS_CODE,
            media_type="application/json",
        )
    raise HTTPException(
        status_code=INTERNAL_SERVER_STATUS_CODE, detail="Unable to register helpseeker"
    )
