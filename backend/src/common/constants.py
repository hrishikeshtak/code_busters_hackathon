"""Constants required in the code"""
import os

AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

# S3 Bucket
BUCKET_NAME = "code-busters-hackathon-22-09-2023"

# DynamoDB Table Name
NAVIGATOR_TABLE_NAME = "navigator"
HELPSEEKER_TABLE_NAME = "helpseeker"
CATEGORY_TABLE_NAME = "category"
ORGANIZATION_TABLE_NAME = "organization"
WORKFLOW_TABLE_NAME = "workflow"

# HTTP Status Code
SUCCESS_STATUS_CODE = 200
BAD_REQUEST = 400
NOT_FOUND = 404
INTERNAL_SERVER_STATUS_CODE = 500
