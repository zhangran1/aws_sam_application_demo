import json
import logging
from constants import *

logger = logging.getLogger()


def http_standard_return(valid_input: bool):
    """
    Construct standard HTTP response based on valid_input.

    Args:
        valid_input: boolean input to indicate true or false of file validation.

    Returns:
        Json response contains the following fields:
        1. statusCode: 200 (File upload successful); 400 (File upload failed);
        2. body: Json data contains return standard message based on valid_input value.
    """

    if valid_input:
        status_code = HTTP_SUCCESS_STATUS
        response_message = SUCCESS_MSG_RESPONSE
    else:
        status_code = HTTP_FAIL_STATUS
        response_message = FAIL_VALIDATION_FAIL

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "message": response_message,
        })}


