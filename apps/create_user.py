import json
import employee

from utils import *
from constants import *

logger = logging.getLogger()


def lambda_handler(event, context):
    """Lambda Function to process create request for single user. User ID shall be passed from path parameter. fields to
    be processed will be passed in from body field. All other three fields are required: login, name, salary

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

    # due to time constrain, assume this input is valid
    # db locking check is not enabled, assume the each time is only one operation taken place
    employee_id = event["pathParameters"]["id"]

    if not event["body"]:
        return http_responses.http_standard_return(False, failed_msg=INVALID_BODY_INPUT)

    if isinstance(event["body"], str):
        try:
            event["body"] = json.loads(event["body"])
        except Exception as e:
            logger.error(e)
            return http_responses.http_standard_return(False, failed_msg=INVALID_BODY_INPUT)


    if not user_cr_validation(event["body"]):
        return http_responses.http_standard_return(False, failed_msg=INVALID_BODY_INPUT)


    login = event["body"]["login"]
    name = event["body"]["name"]
    salary = event["body"]["salary"]

    new_employee = employee.Employee(employee_id, login, name, salary)

    upload_status = database_helper.create_employee(new_employee)

    if upload_status == DB_FAILED_OPERATION:
        return http_responses.http_standard_return(False, failed_msg=INVALID_BODY_INPUT)

    return http_responses.http_standard_return(True, success_msg=VALID_CR_DB_OPERATION)
