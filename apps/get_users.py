import logging
import csv
import http_responses
import multipart_form_parser

from utils import *
from constants import *

logger = logging.getLogger()


def lambda_handler(event, context):
    """Lambda Function to get users information from database.

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

    context: object, required
        Lambda Context runtime methods and attributes

    Returns:
        Json response contains the following fields:
        1. statusCode: 200 (Valid Response); 400 (Invalid Request);
        2. body: list of formatted employee records
    """

    return http_responses.http_standard_return(True)
