"""Constants required in the code"""
import os

AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

# DynamoDB Table Name
NAVIGATOR_TABLE_NAME = "navigator"
HELPSEEKER_TABLE_NAME = "helpseeker"
CATEGORY_TABLE_NAME = "category"
ORGANIZATION_TABLE_NAME = "organization"
WORKFLOW_TABLE_NAME = "workflow"

# HTTP Status Code
SUCCESS_STATUS_CODE = 200
NOT_FOUND = 404
INTERNAL_SERVER_STATUS_CODE = 500
