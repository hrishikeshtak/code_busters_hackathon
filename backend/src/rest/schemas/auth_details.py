from pydantic import BaseModel, field_validator
from datetime import date, datetime
from typing import Optional

DATE_FORMAT = "%Y-%m-%d"


class AuthDetails(BaseModel):
    username: str
    password: str


class NavigatorResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    role: str


class HelpSeeker(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: str
    enrolled_date: str = datetime.today().strftime("%Y-%m-%d")
    location: str
    navigator_id: int
    contact_number: str

    @field_validator("date_of_birth")
    def validate_date_of_birth(cls, value: str) -> str:
        """validate date_of_birth"""
        # Retrieve the value of date_of_birth field from the values dictionary
        try:
            validate_date = datetime.strptime(value, DATE_FORMAT)
            return validate_date.strftime(DATE_FORMAT)
        except ValueError:
            raise ValueError(f"date_of_birth is not in correct format: {DATE_FORMAT}")

    @field_validator("enrolled_date")
    def validate_enrolled_date(cls, value: str) -> str:
        """validate enrolled_date"""
        # Retrieve the value of enrolled_date field from the values dictionary
        try:
            validate_date = datetime.strptime(value, DATE_FORMAT)
            return validate_date.strftime(DATE_FORMAT)
        except ValueError:
            raise ValueError(f"enrolled_date is not in correct format: {DATE_FORMAT}")
