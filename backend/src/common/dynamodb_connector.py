"""DynamoDB Connector"""

import os
from typing import Dict, List, Optional, Tuple

import boto3
from botocore.exceptions import ClientError

from ..common.constants import (AWS_REGION, HELPSEEKER_TABLE_NAME,
                                INTERNAL_SERVER_STATUS_CODE,
                                NAVIGATOR_TABLE_NAME, SUCCESS_STATUS_CODE,
                                WORKFLOW_TABLE_NAME)
from ..common.helper import Helper
from ..rest.schemas.schema import HelpSeeker, NavigatorResponse


class DynamoDBConnector:
    """Dynmano DB Connector"""
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

    def get_last_id_from_dynamodb_table(self, table_name: str) -> int:
        """get last id from dynamodb table"""
        all_items = self.get_all_items_from_table(table_name=table_name)
        last_count = 0
        for item in all_items:
            if item.get("id") > last_count:
                last_count = item.get("id")
        return int(last_count)

    def get_all_items_from_table(self, table_name: str = NAVIGATOR_TABLE_NAME) -> Dict:
        """fetch data from DynamoDB"""
        table = self.dynamodb.Table(table_name)
        response = table.scan()
        data = response["Items"]
        return data

    def add_entry_in_helpseeker(self, help_seeker: HelpSeeker) -> Tuple[int, Dict]:
        """Add entry of help seeker in dynamoDb"""
        # get last id from the HELPSEEKER_TABLE_NAME
        last_id = self.get_last_id_from_dynamodb_table(table_name=HELPSEEKER_TABLE_NAME)
        Helper.print_message(
            f"last id from the {HELPSEEKER_TABLE_NAME} is {last_id}"
        )
        table = self.dynamodb.Table(HELPSEEKER_TABLE_NAME)
        data = help_seeker.model_dump()
        # add id into data as dynamodb using id as partition key
        data["id"] = last_id + 1
        response = table.put_item(Item=data)
        response_metadata = response.get("ResponseMetadata", {})
        if response_metadata.get("HTTPStatusCode") == SUCCESS_STATUS_CODE:
            return SUCCESS_STATUS_CODE, data
        return INTERNAL_SERVER_STATUS_CODE, {}

    def add_entry_in_workflow(self, entries: List[Dict]) -> int:
        """Add entry of workflow in dynamoDb"""
        # get last id from the WORKFLOW_TABLE_NAME
        last_id = self.get_last_id_from_dynamodb_table(table_name=WORKFLOW_TABLE_NAME)
        Helper.print_message(
            f"last id from the {WORKFLOW_TABLE_NAME} is {last_id}"
        )
        table = self.dynamodb.Table(WORKFLOW_TABLE_NAME)
        # add id into data as dynamodb using id as partition key
        try:
            with table.batch_writer() as batch:
                for entry in entries:
                    # update last_id
                    last_id += 1
                    entry["id"] = last_id
                    batch.put_item(Item=entry)
                    return SUCCESS_STATUS_CODE
        except ClientError as err:
            Helper.print_message(
                f"Couldn't add entry in workflow tables. Here's why: "
                f"{err.response['Error']['Code']}: "
                f"{err.response['Error']['Message']}"
            )
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
