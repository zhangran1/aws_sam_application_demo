import logging

import http_responses
import multipart_form_parser

from utils import *

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

    multiform_data = filter_csv_data(event['body'])

    validation = False
    for record in multiform_data[:-1]:
        csv_data = csv.reader(record.splitlines(), delimiter=',')
        ss = multipart_form_parser.UploadDataParser(csv_data)
        validation = ss.valid_input

    return http_responses.http_standard_return(validation)
