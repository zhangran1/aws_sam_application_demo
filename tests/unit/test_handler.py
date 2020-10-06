import sys

sys.path.append('././apps/')

from apps import upload
from apps import get_user_by_id
from apps import create_user
from apps import patch_user
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
    assert data["results"] == FILE_VALIDATION_FAIL
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
    assert data["results"] == FILE_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_case_2(user_input_invalid_test_case_2):
    release_db_lock()
    ret = upload.lambda_handler(user_input_invalid_test_case_2, "")
    data = json.loads(ret["body"])
    assert data["results"] == FILE_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_case_3(user_input_invalid_test_case_3):
    release_db_lock()
    ret = upload.lambda_handler(user_input_invalid_test_case_3, "")
    data = json.loads(ret["body"])
    assert data["results"] == FILE_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_case_4(user_input_invalid_test_case_4):
    release_db_lock()
    ret = upload.lambda_handler(user_input_invalid_test_case_4, "")
    data = json.loads(ret["body"])
    assert data["results"] == FILE_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_duplicate_id_login(user_input_invalid_duplicate_id_login):
    release_db_lock()
    ret = upload.lambda_handler(user_input_invalid_duplicate_id_login, "")
    data = json.loads(ret["body"])
    assert data["results"] == FILE_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_empty_file(user_input_invalid_test_empty_file):
    release_db_lock()
    ret = upload.lambda_handler(user_input_invalid_test_empty_file, "")
    data = json.loads(ret["body"])
    assert data["results"] == FILE_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_check_existing_employee():
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
    assert data["results"] == GET_ID_BY_USER_RESPONSE


def test_retrieve_single_user_from_db_none_exist_user(get_user_by_id_none_exist_user):
    ret = retrieve_user_record_by_id(get_user_by_id_none_exist_user["pathParameters"]["id"])
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 400
    assert "results" in ret["body"]
    assert data["results"] == RETRIEVE_EMPLOYEE_FAILED


def test_get_user_by_id(get_user_by_id_existing_user, get_user_by_id_existing_user_db_record):
    ret = get_user_by_id.lambda_handler(get_user_by_id_existing_user, "")
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 200
    assert "results" in ret["body"]
    assert data["results"] == get_user_by_id_existing_user_db_record


def test_get_user_by_id_invalid_field(get_user_by_id_invalid_id):
    ret = get_user_by_id.lambda_handler(get_user_by_id_invalid_id, "")
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 400
    assert "results" in ret["body"]
    assert data["results"] == RETRIEVE_EMPLOYEE_FAILED


def test_get_user_by_no_id(get_user_by_no_id):
    ret = get_user_by_id.lambda_handler(get_user_by_no_id, "")
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 400
    assert "results" in ret["body"]
    assert data["results"] == RETRIEVE_EMPLOYEE_FAILED


def test_user_cr_validation_valid_case(create_update_user_valid_case):
    ret = user_cr_validation(create_update_user_valid_case["body"])
    assert ret is True


def test_create_update_user_invalid_case_no_login(create_update_user_invalid_case_no_login):
    ret = user_cr_validation(create_update_user_invalid_case_no_login["body"])
    assert ret is False


def test_create_update_user_invalid_case_no_name(create_update_user_invalid_case_no_name):
    ret = user_cr_validation(create_update_user_invalid_case_no_name["body"])
    assert ret is False


def test_create_update_user_invalid_case_no_salary(create_update_user_invalid_case_no_salary):
    ret = user_cr_validation(create_update_user_invalid_case_no_salary["body"])
    assert ret is False


def test_create_update_user_invalid_case_invalid_salary(create_update_user_invalid_case_invalid_salary):
    ret = user_cr_validation(create_update_user_invalid_case_invalid_salary["body"])
    assert ret is False


def test_create_update_user_invalid_salary_negative(create_update_user_invalid_salary_negative):
    ret = user_cr_validation(create_update_user_invalid_salary_negative["body"])
    assert ret is False


def test_create_user_invalid(create_user_invalid_case):
    ret = create_user.lambda_handler(create_user_invalid_case, "")
    data = json.loads(ret["body"])
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 400
    assert "results" in ret["body"]
    assert data["results"] == INVALID_BODY_INPUT


def test_create_user_valid_case(create_user_valid_case):
    # this test case will create a new record and then deleted from database to prevent interrupt other test cases

    create_ret = create_user.lambda_handler(create_user_valid_case, "")
    data = json.loads(create_ret["body"])
    assert create_ret["statusCode"] == 200
    assert "results" in create_ret["body"]
    assert data["results"] == VALID_CR_DB_OPERATION
    # select the record just created
    select_ret = get_user_by_id.lambda_handler(create_user_valid_case, "")
    data = json.loads(select_ret["body"])
    assert select_ret["statusCode"] == 200
    assert "results" in select_ret["body"]
    assert data["results"]["id"] == "z-api-create-user-login"
    assert data["results"]["login"] == "z-api-create-user-login"
    assert data["results"]["name"] == "z-api-create-user-name"
    assert data["results"]["salary"] == '1500.0'

    # physically delete
    delete_ret = db_real_delete_for_testing_purpose(data["results"]["id"])
    data = json.loads(create_ret["body"])
    assert create_ret["statusCode"] == 200

    # validate deletion
    select_ret = get_user_by_id.lambda_handler(create_user_valid_case, "")
    data = json.loads(select_ret["body"])
    assert select_ret["statusCode"] == 400


def test_logical_delete_user(logical_delete_user_valid_case):
    create_ret = create_user.lambda_handler(logical_delete_user_valid_case, "")
    data = json.loads(create_ret["body"])
    assert create_ret["statusCode"] == 200
    assert "results" in create_ret["body"]
    assert data["results"] == VALID_CR_DB_OPERATION

    select_ret = select_ret = get_user_by_id.lambda_handler(logical_delete_user_valid_case, "")
    assert select_ret["statusCode"] == 200

    delete_ret = delete_employee(logical_delete_user_valid_case["pathParameters"]["id"])
    assert delete_ret == DB_SUCCESS_OPERATION

    select_ret = retrieve_user_record_by_id(logical_delete_user_valid_case["pathParameters"]["id"])
    assert select_ret["statusCode"] == 400

    delete_ret = db_real_delete_for_testing_purpose(logical_delete_user_valid_case["pathParameters"]["id"])
    data = json.loads(create_ret["body"])
    assert delete_ret["statusCode"] == 200


def test_patch_none_exit_user(patch_none_exist_user):
    ret = patch_user.lambda_handler(patch_none_exist_user, "")
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 400
    assert data["results"] == USER_DOES_NOT_EXIST_CANNOT_PATCH


def test_patch_valid_user(create_user_valid_case, patch_user_valid_case):
    create_ret = create_user.lambda_handler(create_user_valid_case, "")
    data = json.loads(create_ret["body"])
    assert create_ret["statusCode"] == 200
    assert "results" in create_ret["body"]
    assert data["results"] == VALID_CR_DB_OPERATION
    # select the record just created
    select_ret = get_user_by_id.lambda_handler(create_user_valid_case, "")
    data = json.loads(select_ret["body"])
    assert select_ret["statusCode"] == 200
    assert "results" in select_ret["body"]
    assert data["results"]["id"] == "z-api-create-user-login"
    assert data["results"]["login"] == "z-api-create-user-login"
    assert data["results"]["name"] == "z-api-create-user-name"
    assert data["results"]["salary"] == '1500.0'

    patch_ret = patch_user.lambda_handler(patch_user_valid_case, "")
    data = json.loads(patch_ret["body"])
    assert patch_ret["statusCode"] == 200

    select_ret = get_user_by_id.lambda_handler(create_user_valid_case, "")
    data = json.loads(select_ret["body"])
    assert select_ret["statusCode"] == 200
    assert "results" in select_ret["body"]
    assert data["results"]["id"] == "z-api-create-user-login"
    assert data["results"]["login"] == "test-patch-z-api-create-user-login"
    assert data["results"]["name"] == "test-patch-z-api-create-user-name"
    assert data["results"]["salary"] == '2500.0'

    # physically delete the record to prevent newly insert data affect other test cases
    delete_ret = db_real_delete_for_testing_purpose(data["results"]["id"])
    data = json.loads(create_ret["body"])
    assert delete_ret["statusCode"] == 200

