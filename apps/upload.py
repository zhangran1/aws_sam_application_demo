import os
import json
import logging
import base64
import csv

import http_responses

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

    data = filter_csv_data(event['body'])
    if data:
        validation = True
    else:
        validation = False

    return http_responses.http_standard_return(validation)
