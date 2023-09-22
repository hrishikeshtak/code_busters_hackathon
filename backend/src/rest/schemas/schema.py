"""Pydantic Schmea"""
from datetime import datetime
from enum import Enum
from typing import List, Optional
from decimal import Decimal

import phonenumbers
from pydantic import BaseModel, field_validator

DATE_FORMAT = "%Y-%m-%d"


class AuthDetails(BaseModel):
    """AuthDetails Schema"""
    username: str
    password: str


class NavigatorResponse(BaseModel):
    """NavigatorResponse Schema"""
    id: int
    first_name: str
    last_name: str
    role: str


class HelpSeeker(BaseModel):
    """HelpSeeker Schema"""
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

    @field_validator("contact_number")
    def validate_contact_number(cls, value: str) -> str:
        """validate contact number"""
        try:
            validate_phone = phonenumbers.parse(value)
            if not phonenumbers.is_valid_number(validate_phone):
                raise ValueError(f"Invalid Contact Number: {value}")
            return value
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValueError(f"Invalid Contact Number: {value}")


class EnrolledStatus(str, Enum):
    in_need = "in need"
    not_eligible = "not eligible"
    closed_out = "closed out"


class EnrolledCategory(BaseModel):
    category_id: int
    organization_id: int
    notes: Optional[str] = None
    status: str = EnrolledStatus.in_need
    status_enrolled_date: str = datetime.today().strftime("%Y-%m-%d")


class UserData(BaseModel):
    help_seeker: HelpSeeker
    enrolled_categories: List[EnrolledCategory]


class Category(BaseModel):
    """Category Schema"""
    id: int
    name: str


class Organization(BaseModel):
    """Organization Schema"""
    id: int
    category_id: int
    category_name: str
    name: str
    service: str


class HelpSeekerResponse(BaseModel):
    """HelpSeeker Schema"""
    id: int
    first_name: str
    last_name: str
    date_of_birth: str
    enrolled_date: str = datetime.today().strftime("%Y-%m-%d")
    location: str
    navigator_id: int
    contact_number: str


class WorkflowResponse(BaseModel):
    id: int
    category_id: int
    helpseeker_id: int
    notes: str
    organization_id: int
    status: str
    status_enrolled_date: str
