import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append('././apps/')

import pytest

from tests.unit.test_constants import *

valid_test_case_2 = dir_path + "/sample_test_case/valid_test_case2_with_chinese_character.csv"
invalid_test_case_1 = dir_path + "/sample_test_case/invalid_test_case1_extra_one_column_record.csv"
invalid_test_case_2 = dir_path + "/sample_test_case/invalid_test_case2_missing_one_column_record.csv"
invalid_test_case_3 = dir_path + "/sample_test_case/invalid_test_case3_invalid_salary.csv"
invalid_test_empty_file = dir_path + "/sample_test_case/invalid_test_empty_file.csv"


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
    return {
        "body": valid_test_case_2
    }


@pytest.fixture()
def user_input_valid_test_case_3():
    return {
        "body": None
    }

@pytest.fixture()
def user_input_invalid_test_case_1():
    return {
        "body": invalid_test_case_1
    }


@pytest.fixture()
def user_input_invalid_test_case_2():
    return {
        "body": invalid_test_case_2
    }


@pytest.fixture()
def user_input_invalid_test_case_3():
    return {
        "body": invalid_test_case_3
    }


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
