import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.path.append('././apps/')

import pytest

valid_test_case_1 = dir_path + "/sample_test_case/valid_test_case1.csv"
valid_test_case_2 = dir_path + "/sample_test_case/valid_test_case2.csv"
invalid_test_case_1 = dir_path + "/sample_test_case/invalid_test_case_1.csv"
invalid_test_case_2 = dir_path + "/sample_test_case/invalid_test_case_2.csv"
invalid_test_case_3 = dir_path + "/sample_test_case/invalid_test_case_3.csv"
invalid_test_empty_file = dir_path + "/sample_test_case/invalid_test_empty_file.csv"

@pytest.fixture()
def user_input_valid_test_case_1():

    return {
        "body": valid_test_case_1
    }

@pytest.fixture()
def user_input_valid_test_case_2():

    return {
        "body": valid_test_case_2
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

    return {
        "body": invalid_test_empty_file
    }