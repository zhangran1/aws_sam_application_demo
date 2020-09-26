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
