"""DynamoDB Connector"""

import os
from typing import Dict, Optional
from datetime import date
import boto3
from botocore.exceptions import ClientError

from ..rest.schemas.auth_details import NavigatorResponse, HelpSeeker
from ..common.helper import (
    AWS_REGION,
    Helper,
    NAVIGATOR_TABLE_NAME,
    HELPSEEKER_TABLE_NAME,
    SUCCESS_STATUS_CODE,
    INTERNAL_SERVER_STATUS_CODE,
)


class DynamoDBConnector:
    def __init__(self):
        self.dynamodb = boto3.resource(
            "dynamodb",
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
            region_name=AWS_REGION,
        )
        # self.client = boto3.client("dynamodb", region_name=REGION)

    def authenticate_user(
        self, username: str, password: str, table_name: str = NAVIGATOR_TABLE_NAME
    ) -> NavigatorResponse:
        """authenticate user"""
        response = self.get_navigator_data(username=username, table_name=table_name)
        data = None
        if response:
            # validate password
            if response.get("password") == password:
                data = NavigatorResponse(
                    id=response.get("id"),
                    first_name=response.get("first_name"),
                    last_name=response.get("last_name"),
                    role=response.get("role"),
                )
        return data

    def get_navigator_data(
        self, username: str, table_name: str = NAVIGATOR_TABLE_NAME
    ) -> Optional[Dict]:
        """fetch data from DynamoDB"""
        table = self.dynamodb.Table(table_name)
        response = table.get_item(Key={"username": username})
        if response.get("Item"):
            Helper.print_message(
                f"successfully fetch user data from dynamodb for username: {username}"
            )
        return response.get("Item")

    def get_last_helpseeker_id(self, table_name: str = HELPSEEKER_TABLE_NAME) -> int:
        all_items = self.get_all_items_from_table(table_name=table_name)
        last_count = 0
        for item in all_items:
            if item.get("id") > last_count:
                last_count = item.get("id")
        return int(last_count)

    def get_all_items_from_table(self, table_name: str = NAVIGATOR_TABLE_NAME):
        """fetch data from DynamoDB"""
        table = self.dynamodb.Table(table_name)
        response = table.scan()
        data = response["Items"]
        return data

    def add_entry_in_helpseeker(self):
        last_count = self.get_last_helpseeker_id()
        Helper.print_message(
            f"last_count from the {HELPSEEKER_TABLE_NAME} is {last_count}"
        )
        item = HelpSeeker(
            first_name="test",
            last_name="test",
            date_of_birth="2023-09-22",
            enrolled_date="2023-09-22",
            location="delaware",
            navigator_id=2,
            contact_number="7385685790",
        )
        table = self.dynamodb.Table(HELPSEEKER_TABLE_NAME)
        data = item.model_dump()
        # add id into data as dynamodb using id as partition key
        data["id"] = last_count + 1
        response = table.put_item(Item=data)
        response_metadata = response.get("ResponseMetadata", {})
        if response_metadata.get("HTTPStatusCode") == SUCCESS_STATUS_CODE:
            return SUCCESS_STATUS_CODE
        return INTERNAL_SERVER_STATUS_CODE

    def list_tables(self):
        """
        Lists the Amazon DynamoDB tables for the current account.

        :return: The list of tables.
        """
        try:
            tables = []
            for table in self.dynamodb.tables.all():
                print(table.name)
                tables.append(table)
        except ClientError as err:
            Helper.print_message(
                f"Couldn't list tables. Here's why: "
                f"{err.response['Error']['Code']}: "
                f"{err.response['Error']['Message']}"
            )
            raise
        else:
            return tables


if __name__ == "__main__":
    obj = DynamoDBConnector()
    # obj.list_tables()
    obj.get_all_items_from_table(table_name=HELPSEEKER_TABLE_NAME)
    # obj.get_user_data(username="admin")
