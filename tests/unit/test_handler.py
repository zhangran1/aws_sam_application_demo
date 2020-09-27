import sys

sys.path.append('././apps/')

from apps import upload
from tests.unit.test_cases import *
from tests.unit.test_constants import *
from tests.unit.test_class_setup import *
from apps.http_responses import *
from apps.utils import *
from apps.database_helper import *


def test_http_response_success():
    validation = True
    ret = http_standard_return(validation)
    data = json.loads(ret["body"])
    assert data["message"] == SUCCESS_MSG_RESPONSE
    assert ret["statusCode"] == HTTP_SUCCESS_STATUS


def test_http_response_fail():
    validation = False
    ret = http_standard_return(validation)
    data = json.loads(ret["body"])
    assert data["message"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_filter_csv_data():
    processed_data = filter_csv_data(BINARY_VALID_TEST_CASE_1)
    logger.info(processed_data)
    assert processed_data == VALID_PROCESSED_DATA_TEST_CASE_1


def test_filter_csv_data_test_case_3():
    processed_data = filter_csv_data(BINARY_VALID_TEST_CASE_3)
    logger.info(processed_data)
    assert processed_data == VALID_PROCESSED_DATA_TEST_CASE_3


def test_valid_multi_part_form_parser(valid_upload_data_parser):
    assert valid_upload_data_parser.valid_input is True


def test_invalid_upload_data_parser(invalid_upload_data_parser):
    assert invalid_upload_data_parser.valid_input is False


def test_user_input_valid_test_case_1(user_input_valid_test_case_1):
    ret = upload.lambda_handler(user_input_valid_test_case_1, "")
    data = json.loads(ret["body"])
    assert data["message"] == SUCCESS_MSG_RESPONSE
    assert ret["statusCode"] == HTTP_SUCCESS_STATUS


def test_user_input_valid_test_case_2(user_input_valid_test_case_2):
    ret = upload.lambda_handler(user_input_valid_test_case_2, "")
    data = json.loads(ret["body"])
    assert data["message"] == SUCCESS_MSG_RESPONSE
    assert ret["statusCode"] == HTTP_SUCCESS_STATUS


def test_user_input_valid_test_case_3(user_input_valid_test_case_3):
    ret = upload.lambda_handler(user_input_valid_test_case_3, "")
    data = json.loads(ret["body"])
    assert data["message"] == SUCCESS_MSG_RESPONSE
    assert ret["statusCode"] == HTTP_SUCCESS_STATUS


def test_user_input_invalid_test_case_1(user_input_invalid_test_case_1):
    ret = upload.lambda_handler(user_input_invalid_test_case_1, "")
    data = json.loads(ret["body"])
    assert data["message"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_case_2(user_input_invalid_test_case_2):
    ret = upload.lambda_handler(user_input_invalid_test_case_2, "")
    data = json.loads(ret["body"])
    assert data["message"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_case_3(user_input_invalid_test_case_3):
    ret = upload.lambda_handler(user_input_invalid_test_case_3, "")
    data = json.loads(ret["body"])
    assert data["message"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_case_4(user_input_invalid_test_case_4):
    ret = upload.lambda_handler(user_input_invalid_test_case_4, "")
    data = json.loads(ret["body"])
    assert data["message"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_duplicate_id_login(user_input_invalid_duplicate_id_login):
    ret = upload.lambda_handler(user_input_invalid_duplicate_id_login, "")
    data = json.loads(ret["body"])
    assert data["message"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_empty_file(user_input_invalid_test_empty_file):
    ret = upload.lambda_handler(user_input_invalid_test_empty_file, "")
    data = json.loads(ret["body"])
    assert data["message"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_check_existing_employee():
    current_employee_id = EXISTING_EMPLOYEE
    record_count = check_existing_employee(current_employee_id)
    assert record_count == 1
    new_employee_id = NONE_EXIST_EMPLOYEE
    record_count = check_existing_employee(new_employee_id)
    assert record_count == 0


def test_employee_creation(employee_object):
    assert employee_object.employee_id == "test00001"
    assert employee_object.login == "john1"
    assert employee_object.name == "John Smith"
    assert employee_object.salary == 100.5


def test_create_single_employee_record(employee_object):
    ret = create_employee(employee_object)
    assert ret == DB_SUCCESS_OPERATION


def test_create_multiple_employee_records(valid_employee_records):
    ret = upload_csv_record_to_db(valid_employee_records)
    assert ret == DB_SUCCESS_OPERATION
