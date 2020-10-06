import sys
import os
import pytest

from tests.unit.test_constants import *

dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append('././apps/')


@pytest.fixture()
def user_input_valid_test_case_1():
    """
    This is a valid test case
    Content-Encoding: utf-8
    Content-Type: application/x-www-form-urlencoded

    multi-form data:
        file: content of valid_test_case1_with_hash.csv
    """
    valid_test_case_1 = TEST_CASE_TEMPLATE
    valid_test_case_1["body"] = BINARY_VALID_TEST_CASE_1
    return valid_test_case_1


@pytest.fixture()
def user_input_valid_test_case_2():
    """
    This is a valid test case
    Content-Encoding: utf-8
    Content-Type: application/x-www-form-urlencoded

    multi-form data:
        file: content of valid_test_case2_with_chinese_character.csv
    """
    valid_test_case_2 = TEST_CASE_TEMPLATE
    valid_test_case_2["body"] = BINARY_VALID_TEST_CASE_2
    return valid_test_case_2


@pytest.fixture()
def user_input_valid_test_case_3():
    """
    This is a valid test case
    Content-Encoding: utf-8
    Content-Type: application/x-www-form-urlencoded

    multi-form data:
        file: content of valid_test_case3_with_last_line_empty.csv
    """
    valid_test_case_3 = TEST_CASE_TEMPLATE
    valid_test_case_3["body"] = BINARY_VALID_TEST_CASE_3
    return valid_test_case_3


@pytest.fixture()
def user_input_invalid_test_case_1():
    """
    This is a valid test case
    Content-Encoding: utf-8
    Content-Type: application/x-www-form-urlencoded

    multi-form data:
        file: content of invalid_test_case1_extra_one_column_record.csv
    """
    invalid_test_case_1 = TEST_CASE_TEMPLATE
    invalid_test_case_1["body"] = BINARY_INVALID_TEST_CASE_1
    return invalid_test_case_1


@pytest.fixture()
def user_input_invalid_test_case_2():
    """
    This is a valid test case
    Content-Encoding: utf-8
    Content-Type: application/x-www-form-urlencoded

    multi-form data:
        file: content of invalid_test_case2_missing_one_column_record.csv
    """
    invalid_test_case_2 = TEST_CASE_TEMPLATE
    invalid_test_case_2["body"] = BINARY_INVALID_TEST_CASE_2
    return invalid_test_case_2


@pytest.fixture()
def user_input_invalid_test_case_3():
    """
    This is a valid test case
    Content-Encoding: utf-8
    Content-Type: application/x-www-form-urlencoded

    multi-form data:
        file: content of invalid_test_case3_invalid_salary.csv
    """
    invalid_test_case_3 = TEST_CASE_TEMPLATE
    invalid_test_case_3["body"] = BINARY_INVALID_TEST_CASE_3
    return invalid_test_case_3


@pytest.fixture()
def user_input_invalid_test_case_4():
    """
    This is a valid test case
    Content-Encoding: utf-8
    Content-Type: application/x-www-form-urlencoded

    multi-form data:
        file: content of invalid_test_case4_negative_salary.csv
    """
    invalid_test_case_4 = TEST_CASE_TEMPLATE
    invalid_test_case_4["body"] = BINARY_INVALID_TEST_CASE_4
    return invalid_test_case_4


@pytest.fixture()
def user_input_invalid_duplicate_id_login():
    """
    This is a valid test case
    Content-Encoding: utf-8
    Content-Type: application/x-www-form-urlencoded

    multi-form data:
        file: content of invalid_test_case_duplicate_id_login.csv
    """
    invalid_duplicate_id_login = TEST_CASE_TEMPLATE
    invalid_duplicate_id_login["body"] = BINARY_INVALID_DUPLICATE_ID
    return invalid_duplicate_id_login


@pytest.fixture()
def user_input_invalid_test_empty_file():
    """
    This is a invalid test case with empty csv file uploaded
    Content-Encoding: utf-8
    Content-Type: application/x-www-form-urlencoded

    multi-form data:
        file: content of invalid_test_empty_file.csv
    """
    empty_file_test_case = TEST_CASE_TEMPLATE
    empty_file_test_case["body"] = BINARY_INVALID_EMPTY_FILE
    return empty_file_test_case


@pytest.fixture()
def sample_lock_id():
    return SAMPLE_LOCK_ID


@pytest.fixture()
def valid_requested_params():
    return VALID_REQUIRED_PARAMS


@pytest.fixture()
def invalid_requested_params():
    return INVALID_REQUIRED_PARAMS


@pytest.fixture()
def invalid_required_params_negative_min_salary():
    return INVALID_REQUIRED_PARAMS_NEGATIVE_MIN_SALARY


@pytest.fixture()
def invalid_required_params_negative_salary():
    return INVALID_REQUIRED_PARAMS_NEGATIVE_SALARY


@pytest.fixture()
def invalid_required_params_offset():
    return INVALID_REQUIRED_PARAMS_OFFSET


@pytest.fixture()
def invalid_required_params_limit():
    return INVALID_REQUIRED_PARAMS_LIMIT


@pytest.fixture()
def invalid_required_params_sort_sign():
    return INVALID_REQUIRED_PARAMS_SORT_SIGN


@pytest.fixture()
def invalid_required_params_sort_value_case_1():
    return INVALID_REQUIRED_PARAMS_SORT_VALUE_CASE_1


@pytest.fixture()
def invalid_required_params_sort_value_case_2():
    return INVALID_REQUIRED_PARAMS_SORT_VALUE_CASE_2


@pytest.fixture()
def valid_required_params_asc_name():
    return VALID_REQUIRED_PARAMS_ASC_NAME


@pytest.fixture()
def valid_required_params_desc_salary():
    return VALID_REQUIRED_PARAMS_DESC_SALARY


@pytest.fixture()
def valid_required_params_asc_employee_id():
    return VALID_REQUIRED_PARAMS_ASC_EMPLOYEE_ID


@pytest.fixture()
def valid_required_params_desc_login():
    return VALID_REQUIRED_PARAMS_DESC_LOGIN


@pytest.fixture()
def get_user_by_id_existing_user():
    return {
        "pathParameters": {"id": EXISTING_EMPLOYEE},
    }


@pytest.fixture()
def get_user_by_id_none_exist_user():
    return {
        "pathParameters": {"id": NONE_EXIST_EMPLOYEE},
    }


@pytest.fixture()
def get_user_by_id_invalid_id():
    return {
        "pathParameters": {"id": None},
    }


@pytest.fixture()
def get_user_by_no_id():
    return {
        "pathParameters": {},
    }


@pytest.fixture()
def create_update_user_valid_case():
    return {
        "pathParameters": {"id": "api-create-user-login"},
        "body": {
            "login": "api-create-user-login",
            "name": "api-create-user-name",
            "salary": 1500.0
        }
    }


@pytest.fixture()
def create_update_user_invalid_case_no_login():
    return {
        "pathParameters": {"id": "api-create-user-login"},
        "body": {
            "name": "api-create-user-name",
            "salary": 1500.0
        }
    }


@pytest.fixture()
def create_update_user_invalid_case_no_name():
    return {
        "pathParameters": {"id": "api-create-user-login"},
        "body": {
            "login": "api-create-user-login",
            "salary": 1500.0
        }
    }


@pytest.fixture()
def create_update_user_invalid_case_no_salary():
    return {
        "pathParameters": {"id": "api-create-user-login"},
        "body": {
            "login": "api-create-user-login",
            "name": "api-create-user-name",
        }
    }


@pytest.fixture()
def create_update_user_invalid_case_invalid_salary():
    return {
        "pathParameters": {"id": "api-create-user-login"},
        "body": {
            "login": "api-create-user-login",
            "name": "api-create-user-name",
            "salary": "this is in valid salary"
        }
    }


@pytest.fixture()
def create_update_user_invalid_salary_negative():
    return {
        "pathParameters": {"id": "api-create-user-login"},
        "body": {
            "login": "api-create-user-login",
            "name": "api-create-user-name",
            "salary": -1.0
        }
    }


@pytest.fixture()
def create_user_invalid_case():
    return {
        "pathParameters": {"id": "api-create-user-login"},
        "body": {
            "login": "api-create-user-login",
            "name": "api-create-user-name",
            "salary": -1500.0
        }
    }

@pytest.fixture()
def create_user_valid_case():
    return {
        "pathParameters": {"id": "z-api-create-user-login"},
        "body": {
            "login": "z-api-create-user-login",
            "name": "z-api-create-user-name",
            "salary": 1500.0
        }
    }


@pytest.fixture()
def logical_delete_user_valid_case():
    return {
        "pathParameters": {"id": "z-api-create-user-login"},
        "body": {
            "login": "z-api-create-user-login",
            "name": "z-api-create-user-name",
            "salary": 1500.0
        }
    }


@pytest.fixture()
def patch_none_exist_user():
    return {
        "pathParameters": {"id": NONE_EXIST_EMPLOYEE},
    }


@pytest.fixture()
def get_user_by_id_existing_user_db_record():
    return {'id': 'test00001', 'name': 'John Smith', 'login': 'john1', 'salary': '101.5'}


@pytest.fixture()
def patch_user_valid_case():
    return {
        "pathParameters": {"id": "z-api-create-user-login"},
        "body": {
            "login": "test-patch-z-api-create-user-login",
            "name": "test-patch-z-api-create-user-name",
            "salary": 2500.0
        }
    }

