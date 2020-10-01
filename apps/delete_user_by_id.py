from utils import *

logger = logging.getLogger()


def lambda_handler(event, context):
    """Lambda Function to delete single user. User ID shall be passed from path parameter.

   Args:
    event: dict, required
        API Gateway Lambda Proxy Input Format

    context: object, required
        Lambda Context runtime methods and attributes

    Returns:
        Json response contains the following fields:
        1. statusCode: 200 (Valid Response); 400 (Invalid Request);
        2. body: Json data contains return standard message.
    """
    if not event["pathParameters"]:
        return http_responses.http_standard_return(False, failed_msg=DELETE_EMPLOYEE_FAILED)

    if not event["pathParameters"]["id"]:
        http_responses.http_standard_return(False, failed_msg=DELETE_EMPLOYEE_FAILED)

    db_delete_operation = delete_employee(event["pathParameters"]["id"])

    if db_delete_operation != DB_SUCCESS_OPERATION:
        return http_responses.http_standard_return(False, failed_msg=DB_FAILED_OPERATION)

    return http_responses.http_standard_return(True, success_msg=DB_SUCCESS_OPERATION)
