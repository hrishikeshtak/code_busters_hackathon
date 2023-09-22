"""DynamoDB Connector"""

import os
from typing import Dict, Optional
import boto3
from botocore.exceptions import ClientError

from ..rest.schemas.auth_details import NavigatorResponse
from ..common.helper import REGION, Helper, NAVIGATOR_TABLE_NAME


class DynamoDBConnector:
    def __init__(self):
        self.dynamodb = boto3.resource(
            "dynamodb",
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
            region_name=REGION,
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

    def get_all_items_from_table(self, table_name: str = NAVIGATOR_TABLE_NAME):
        """fetch data from DynamoDB"""
        table = self.dynamodb.Table(table_name)
        response = table.scan()
        data = response["Items"]
        print(f"get_all_items_from_table: {data}")
        return data

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
    # obj.get_all_items_from_table()
    obj.get_user_data(username="admin")
