from utils import *
from constants import *

logger = logging.getLogger()


def lambda_handler(event, context):
    """Lambda Function to get users information from database.

   Args:
    event: dict, required
        API Gateway Lambda Proxy Input Format

    context: object, required
        Lambda Context runtime methods and attributes

    Returns:
        Json response contains the following fields:
        1. statusCode: 200 (Valid Response); 400 (Invalid Request);
        2. body: list of formatted employee records
    """
    query_string = event["queryStringParameters"]

    validate_all_request_param = requested_params_validation(query_string)

    if not validate_all_request_param:
        return http_responses.http_standard_return(validate_all_request_param, failed_msg=RETRIEVE_EMPLOYEE_FAILED)

    return database_helper.retrieve_users_from_db(query_string)
