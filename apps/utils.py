import base64
import decimal
import database_helper

from constants import *
from database_helper import *

logger = logging.getLogger()


def filter_csv_data(multi_form_data):
    """Process event body input and return processed data.
    Original raw data format for multi-format data:
        --------------------123456789
        data content one
        --------------------123456789
        data content two
        --------------------123456789
    After split the data, list of record will be returned
        [data content one, data content two]

    Args:
        multi_form_data (string): Even body.

    Returns:
        Json response contains the following fields:
        0. status: failed.
        1. statusCode: 400 (Client side error)
        2. body: Json data contains return message.

    """
    post_data = base64.b64decode(multi_form_data)
    headers, data = post_data.decode('utf-8').split('\r\n', 1)
    data = data.split(headers)
    return data


def upload_csv_record_to_db(employee_records):
    """Handle employee records upload

        Args:
        employee_records (List): list of employee records.

        Returns response message to indicate the status of database operation:
         1. DB_FAILED_OPERATION: Failed
         2. DB_SUCCESS_OPERATION: OK
    """
    upload_status = DB_FAILED_OPERATION
    database_helper.get_db_lock()
    for single_employee_record in employee_records:
        upload_status = database_helper.create_employee(single_employee_record)
        if upload_status == DB_FAILED_OPERATION:
            break
    database_helper.release_db_lock()

    return upload_status


def get_db_lock_status(db_lock=database_lock_id):
    return check_db_lock(db_lock)


def requested_params_validation(requested_params):
    """Validate query string fields and parameter types

        Args:
        requested_params (Dict): Request parameters include the following fields with restrictions:
                    1.minSalary: assume only take in integer minimum value is 0
                    2.maxSalary: integer
                    3.offset: integer minimum value is 0
                    4.limit: 1 to 30 integer value
                    5.sort: String start with "-" or "+", only can sort by "id", "name", "login", "salary"

        Returns response message to indicate the status of database operation:
         1. Valid query string: True
         2. Invalid query string: False
    """
    invalid = False
    valid = True
    validate_all_request_param = all(
        param in requested_params.keys() and len(requested_params[param]) > 0 for param in REQUIRED_PARAMS)

    if not validate_all_request_param:
        return invalid

    try:
        min_salary = int(requested_params["minSalary"])
        max_salary = int(requested_params["maxSalary"])
        offset = int(requested_params["offset"])
        limit = int(requested_params["limit"])
    except ValueError:
        return invalid

    if min_salary < 0:
        return invalid
    if max_salary < 0:
        return invalid
    if offset < 0:
        return invalid
    if limit <= 0 or limit > 30:
        return invalid

    if requested_params["sort"][0] not in ["+", "-", " "]:
        return invalid
    if requested_params["sort"][1:] not in ["id", "name", "login", "salary"]:
        return invalid

    return valid


def user_cr_validation(body_payload):
    """Validate new user creation and update(path)

        Args:
        body_payload (Dict): employee login, name and salary shall pass in via body payload

        Returns response message to indicate the status of database operation:
         1. Valid query string: True
         2. Invalid query string: False
    """

    invalid = False
    valid = True

    # slightly different validation mechanism, value length validation is removed, assume valid salary data is double
    validate_all_request_param = all(
        param in body_payload.keys() for param in REQUIRED_EMPLOYEE_DATA)

    if not validate_all_request_param:
        return invalid

    salary = body_payload["salary"]

    try:
        decimal.Decimal(salary)
    except decimal.InvalidOperation:
        return invalid

    if salary < 0:
        return invalid

    return valid
