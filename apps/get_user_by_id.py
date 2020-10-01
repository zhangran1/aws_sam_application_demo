from utils import *
from constants import *

logger = logging.getLogger()


def lambda_handler(event, context):
    """Lambda Function to get record for single user. User ID shall be passed from path parameter.

   Args:
    event: dict, required
        API Gateway Lambda Proxy Input Format

    context: object, required
        Lambda Context runtime methods and attributes

    Returns:
        Json response contains the following fields:
        1. statusCode: 200 (Valid Response); 400 (Invalid Request);
        2. body: Single employee records if statusCode is 200, fail response message will return if statusCode is 400.
    """

    if not event["pathParameters"]:
        return http_responses.http_standard_return(False, failed_msg=RETRIEVE_EMPLOYEE_FAILED)

    if not event["pathParameters"]["id"]:
        http_responses.http_standard_return(False, failed_msg=RETRIEVE_EMPLOYEE_FAILED)

    return database_helper.retrieve_user_record_by_id(event["pathParameters"]["id"])
