import sys
import os
import requests
import logging

logger = logging.getLogger()

dir_path = os.path.dirname(os.path.realpath(__file__))

from tests.unit.test_constants import *
from tests.unit.test_cases import *

HEADERS = {'Content-Type': 'multipart/form-data', 'Content-Encoding': 'utf-8'}
FILE_UPLOAD_URL = "http://127.0.0.1:3000/users/upload"
GET_EMPLOYEE_URL = "http://127.0.0.1:3000/users"

API_VALID_TEST_CASE_1 = dir_path + "/sample_test_case/valid_test_case1_with_hash.csv"
API_VALID_TEST_CASE_2 = dir_path + "/sample_test_case/valid_test_case2_with_chinese_character.csv"
API_VALID_TEST_CASE_3 = dir_path + "/sample_test_case/valid_test_case3_with_last_line_empty.csv"
API_INVALID_TEST_CASE_1 = dir_path + "/sample_test_case/invalid_test_case1_extra_one_column_record.csv"
API_INVALID_TEST_CASE_2 = dir_path + "/sample_test_case/invalid_test_case2_missing_one_column_record.csv"
API_INVALID_TEST_CASE_3 = dir_path + "/sample_test_case/invalid_test_case3_invalid_salary.csv"
API_INVALID_TEST_CASE_4 = dir_path + "/sample_test_case/invalid_test_case4_negative_salary.csv"
API_INVALID_TEST_EMPTY_FILE = dir_path + "/sample_test_case/invalid_test_empty_file.csv"
API_INVALID_DUPLICATE_ID_LOGIN = dir_path + "/sample_test_case/invalid_test_case_duplicate_id_login.csv"

def get_files(file_name):
    return {
        'file': (file_name, open(file_name, 'rb'), 'text/csv')
    }


def test_api_valid_test_case_1():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(API_VALID_TEST_CASE_1), verify=False)
    assert ret.status_code == HTTP_SUCCESS_STATUS
    assert ret.json()["results"] == SUCCESS_MSG_RESPONSE


def test_api_valid_test_case_2():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(API_VALID_TEST_CASE_2), verify=False)
    assert ret.status_code == HTTP_SUCCESS_STATUS
    assert ret.json()["results"] == SUCCESS_MSG_RESPONSE


def test_api_valid_test_case_3():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(API_VALID_TEST_CASE_3), verify=False)
    assert ret.status_code == HTTP_SUCCESS_STATUS
    assert ret.json()["results"] == SUCCESS_MSG_RESPONSE


def test_api_invalid_test_case_1():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(API_INVALID_TEST_CASE_1), verify=False)
    assert ret.status_code == HTTP_FAIL_STATUS
    assert ret.json()["results"] == FAIL_VALIDATION_FAIL


def test_api_invalid_test_case_2():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(API_INVALID_TEST_CASE_2), verify=False)
    assert ret.status_code == HTTP_FAIL_STATUS
    assert ret.json()["results"] == FAIL_VALIDATION_FAIL


def test_api_invalid_test_case_3():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(API_INVALID_TEST_CASE_3), verify=False)
    assert ret.status_code == HTTP_FAIL_STATUS
    assert ret.json()["results"] == FAIL_VALIDATION_FAIL


def test_api_invalid_duplicate_login():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(API_INVALID_TEST_CASE_4), verify=False)
    assert ret.status_code == HTTP_FAIL_STATUS
    assert ret.json()["results"] == FAIL_VALIDATION_FAIL


def test_api_invalid_empty_file():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(API_INVALID_TEST_EMPTY_FILE), verify=False)
    assert ret.status_code == HTTP_FAIL_STATUS
    assert ret.json()["results"] == FAIL_VALIDATION_FAIL


def test_api_invalid_duplicate_id_login():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(API_INVALID_DUPLICATE_ID_LOGIN), verify=False)
    assert ret.status_code == HTTP_FAIL_STATUS
    assert ret.json()["results"] == FAIL_VALIDATION_FAIL


def test_invalid_requested_params(invalid_requested_params):
    ret = requests.get(GET_EMPLOYEE_URL, params=invalid_requested_params)
    assert ret.status_code == HTTP_FAIL_STATUS


def test_invalid_required_params_negative_min_salary(invalid_required_params_negative_min_salary):
    ret = requests.get(GET_EMPLOYEE_URL, params=invalid_required_params_negative_min_salary)
    assert ret.status_code == HTTP_FAIL_STATUS


def test_invalid_required_params_negative_salary(invalid_required_params_negative_salary):
    ret = requests.get(GET_EMPLOYEE_URL, params=invalid_required_params_negative_salary)
    assert ret.status_code == HTTP_FAIL_STATUS


def test_invalid_required_params_offset(invalid_required_params_offset):
    ret = requests.get(GET_EMPLOYEE_URL, params=invalid_required_params_offset)
    assert ret.status_code == HTTP_FAIL_STATUS


def test_invalid_required_params_limit(invalid_required_params_limit):
    ret = requests.get(GET_EMPLOYEE_URL, params=invalid_required_params_limit)
    assert ret.status_code == HTTP_FAIL_STATUS


def test_invalid_required_params_sort_sign(invalid_required_params_sort_sign):
    ret = requests.get(GET_EMPLOYEE_URL, params=invalid_required_params_sort_sign)
    assert ret.status_code == HTTP_FAIL_STATUS


def test_invalid_required_params_sort_value_case_1(invalid_required_params_sort_value_case_1):
    ret = requests.get(GET_EMPLOYEE_URL, params=invalid_required_params_sort_value_case_1)
    assert ret.status_code == HTTP_FAIL_STATUS


def test_invalid_required_params_sort_value_case_2(invalid_required_params_sort_value_case_2):
    ret = requests.get(GET_EMPLOYEE_URL, params=invalid_required_params_sort_value_case_2)
    assert ret.status_code == HTTP_FAIL_STATUS


def test_valid_required_params_asc_name(valid_required_params_asc_name):
    ret = requests.get(GET_EMPLOYEE_URL, params=valid_required_params_asc_name)
    assert ret.status_code == HTTP_SUCCESS_STATUS
    assert ret.json()["results"] == VALID_REQUIRED_PARAMS_ASC_NAME_RECORD


def test_valid_required_params_desc_salary(valid_required_params_desc_salary):
    ret = requests.get(GET_EMPLOYEE_URL, params=valid_required_params_desc_salary)
    assert ret.status_code == HTTP_SUCCESS_STATUS
    assert ret.json()["results"] == VALID_REQUIRED_PARAMS_DESC_SALARY_RECORD


def test_valid_required_params_asc_employee_id(valid_required_params_asc_employee_id):
    ret = requests.get(GET_EMPLOYEE_URL, params=valid_required_params_asc_employee_id)
    assert ret.status_code == HTTP_SUCCESS_STATUS
    assert ret.json()["results"] == VALID_REQUIRED_PARAMS_ASC_EMPLOYEE_ID_RECORD


def test_valid_required_params_desc_login(valid_required_params_desc_login):
    ret = requests.get(GET_EMPLOYEE_URL, params=valid_required_params_desc_login)
    assert ret.status_code == HTTP_SUCCESS_STATUS
    assert ret.json()["results"] == VALID_REQUIRED_PARAMS_DESC_LOGIN_RECORD
