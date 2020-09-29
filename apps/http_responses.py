import json
import logging
from constants import *

logger = logging.getLogger()


def http_standard_return(valid_input: bool, success_msg=SUCCESS_MSG_RESPONSE, failed_msg=FILE_VALIDATION_FAIL):
    """
    Construct standard HTTP response based on valid_input.

    Args:
        valid_input: boolean input to indicate true or false of file validation.
        success_msg: Successful message, default "File uploaded successfully"
        failed_msg: Failed upload message, default "File Validation Failed"

    Returns:
        Json response contains the following fields:
        1. statusCode: 200 (File upload successful); 400 (File upload failed);
        2. body: Json data contains return standard message based on valid_input value.
    """

    if valid_input:
        status_code = HTTP_SUCCESS_STATUS
        response_message = success_msg
    else:
        status_code = HTTP_FAIL_STATUS
        response_message = failed_msg

    return {
        "statusCode": status_code,
        "body": json.dumps({
            "results": response_message,
        })}


