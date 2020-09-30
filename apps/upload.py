import csv
import multipart_form_parser

from utils import *
from constants import *

logger = logging.getLogger()


def lambda_handler(event, context):
    """Lambda Function to handle user upload csv files.

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

    context: object, required
        Lambda Context runtime methods and attributes

    Returns:
        Json response contains the following fields:
        1. statusCode: 200 (File upload successful); 400 (File upload failed);
        2. body: Json data contains return standard message based on valid_input value.
    """
    db_lock_status = get_db_lock_status()
    if db_lock_status:
        # if db lock is in use, return error message to indicate that the current upload cannot be proceed
        http_status = False
        current_upload_error_msg = "Another file is being processed, upload failed"
        return http_responses.http_standard_return(http_status, failed_msg=current_upload_error_msg)

    multiform_data = filter_csv_data(event['body'])

    validation = False
    for record in multiform_data[:-1]:
        csv_data = csv.reader(record.splitlines(), delimiter=',')
        user_data = multipart_form_parser.UploadDataParser(csv_data)
        validation = user_data.valid_input
        if validation:
            process_status = upload_csv_record_to_db(user_data.employee_record)
            if process_status == DB_FAILED_OPERATION:
                validation = False

    return http_responses.http_standard_return(validation)
