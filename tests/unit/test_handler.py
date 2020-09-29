import sys

sys.path.append('././apps/')

from apps import upload
from apps import get_user_by_id
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
    assert data["results"] == SUCCESS_MSG_RESPONSE
    assert ret["statusCode"] == HTTP_SUCCESS_STATUS


def test_http_response_fail():
    validation = False
    ret = http_standard_return(validation)
    data = json.loads(ret["body"])
    assert data["results"] == FAIL_VALIDATION_FAIL
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
    release_db_lock()
    ret = upload.lambda_handler(user_input_valid_test_case_1, "")
    data = json.loads(ret["body"])
    assert data["results"] == SUCCESS_MSG_RESPONSE
    assert ret["statusCode"] == HTTP_SUCCESS_STATUS


def test_user_input_valid_test_case_2(user_input_valid_test_case_2):
    release_db_lock()
    ret = upload.lambda_handler(user_input_valid_test_case_2, "")
    data = json.loads(ret["body"])
    assert data["results"] == SUCCESS_MSG_RESPONSE
    assert ret["statusCode"] == HTTP_SUCCESS_STATUS


def test_user_input_valid_test_case_3(user_input_valid_test_case_3):
    release_db_lock()
    ret = upload.lambda_handler(user_input_valid_test_case_3, "")
    data = json.loads(ret["body"])
    assert data["results"] == SUCCESS_MSG_RESPONSE
    assert ret["statusCode"] == HTTP_SUCCESS_STATUS


def test_user_input_invalid_test_case_1(user_input_invalid_test_case_1):
    release_db_lock()
    ret = upload.lambda_handler(user_input_invalid_test_case_1, "")
    data = json.loads(ret["body"])
    assert data["results"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_case_2(user_input_invalid_test_case_2):
    release_db_lock()
    ret = upload.lambda_handler(user_input_invalid_test_case_2, "")
    data = json.loads(ret["body"])
    assert data["results"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_case_3(user_input_invalid_test_case_3):
    release_db_lock()
    ret = upload.lambda_handler(user_input_invalid_test_case_3, "")
    data = json.loads(ret["body"])
    assert data["results"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_case_4(user_input_invalid_test_case_4):
    release_db_lock()
    ret = upload.lambda_handler(user_input_invalid_test_case_4, "")
    data = json.loads(ret["body"])
    assert data["results"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_duplicate_id_login(user_input_invalid_duplicate_id_login):
    release_db_lock()
    ret = upload.lambda_handler(user_input_invalid_duplicate_id_login, "")
    data = json.loads(ret["body"])
    assert data["results"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_empty_file(user_input_invalid_test_empty_file):
    release_db_lock()
    ret = upload.lambda_handler(user_input_invalid_test_empty_file, "")
    data = json.loads(ret["body"])
    assert data["results"] == FAIL_VALIDATION_FAIL
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


def test_get_db_lock_release_process(sample_lock_id):
    get_lock_ret = get_db_lock(sample_lock_id)
    assert get_lock_ret == DB_SUCCESS_OPERATION
    lock_status_ret = check_db_lock(sample_lock_id)
    assert lock_status_ret is True
    release_lock_ret = release_db_lock(sample_lock_id)
    assert release_lock_ret == DB_SUCCESS_OPERATION
    ret = check_db_lock(sample_lock_id)
    assert ret is False


def test_release_db_lock_get_process(sample_lock_id):
    release_lock_ret = release_db_lock(sample_lock_id)
    assert release_lock_ret == DB_SUCCESS_OPERATION
    ret = check_db_lock(sample_lock_id)
    assert ret is False
    get_lock_ret = get_db_lock(sample_lock_id)
    assert get_lock_ret == DB_SUCCESS_OPERATION
    lock_status_ret = check_db_lock(sample_lock_id)
    assert lock_status_ret is True


def test_query_string_valid_case(valid_requested_params):
    ret = requested_params_validation(valid_requested_params)
    assert ret is True


def test_invalid_requested_params(invalid_requested_params):
    ret = requested_params_validation(invalid_requested_params)
    assert ret is False


def test_invalid_required_params_negative_min_salary(invalid_required_params_negative_min_salary):
    ret = requested_params_validation(invalid_required_params_negative_min_salary)
    assert ret is False


def test_invalid_required_params_negative_salary(invalid_required_params_negative_salary):
    ret = requested_params_validation(invalid_required_params_negative_salary)
    assert ret is False


def test_invalid_required_params_offset(invalid_required_params_offset):
    ret = requested_params_validation(invalid_required_params_offset)
    assert ret is False


def test_invalid_required_params_limit(invalid_required_params_limit):
    ret = requested_params_validation(invalid_required_params_limit)
    assert ret is False


def test_invalid_required_params_sort_sign(invalid_required_params_sort_sign):
    ret = requested_params_validation(invalid_required_params_sort_sign)
    assert ret is False


def test_invalid_required_params_sort_value_case_1(invalid_required_params_sort_value_case_1):
    ret = requested_params_validation(invalid_required_params_sort_value_case_1)
    assert ret is False


def test_invalid_required_params_sort_value_case_2(invalid_required_params_sort_value_case_2):
    ret = requested_params_validation(invalid_required_params_sort_value_case_2)
    assert ret is False


def test_select_employee_asc_name(valid_required_params_asc_name):
    ret = retrieve_users_from_db(valid_required_params_asc_name)
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 200

    assert data["results"] == VALID_REQUIRED_PARAMS_ASC_NAME_RECORD


def test_select_employee_desc_salary(valid_required_params_desc_salary):
    ret = retrieve_users_from_db(valid_required_params_desc_salary)
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 200
    assert "results" in ret["body"]
    assert data["results"] == VALID_REQUIRED_PARAMS_DESC_SALARY_RECORD


def test_select_employee_asc_id(valid_required_params_asc_employee_id):
    ret = retrieve_users_from_db(valid_required_params_asc_employee_id)
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 200
    assert "results" in ret["body"]
    assert data["results"] == VALID_REQUIRED_PARAMS_ASC_EMPLOYEE_ID_RECORD


def test_select_employee_desc_login(valid_required_params_desc_login):
    ret = retrieve_users_from_db(valid_required_params_desc_login)
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 200
    assert "results" in ret["body"]
    assert data["results"] == VALID_REQUIRED_PARAMS_DESC_LOGIN_RECORD


def test_retrieve_single_user_from_db(get_user_by_id_existing_user):
    ret = retrieve_user_record_by_id(get_user_by_id_existing_user["pathParameters"]["id"])
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 200
    assert "results" in ret["body"]
    assert data["results"] == {'id': 'test00001', 'name': 'John Smith', 'login': 'john1', 'salary': '101.5'}


def test_retrieve_single_user_from_db_none_exist_user(get_user_by_id_none_exist_user):
    ret = retrieve_user_record_by_id(get_user_by_id_none_exist_user["pathParameters"]["id"])
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 400
    assert "results" in ret["body"]
    assert data["results"] == RETRIEVE_EMPLOYEE_FAILED







