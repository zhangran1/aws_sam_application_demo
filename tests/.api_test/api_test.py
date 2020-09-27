import sys
import os
import requests

dir_path = os.path.dirname(os.path.realpath(__file__))

from tests.unit.test_constants import *

HEADERS = {'Content-Type': 'multipart/form-data', 'Content-Encoding': 'utf-8'}
FILE_UPLOAD_URL = "http://127.0.0.1:3000/users/upload"

VALID_TEST_CASE_1 = dir_path + "/sample_test_case/valid_test_case1_with_hash.csv"
VALID_TEST_CASE_2 = dir_path + "/sample_test_case/valid_test_case2_with_chinese_character.csv"
VALID_TEST_CASE_3 = dir_path + "/sample_test_case/valid_test_case3_with_last_line_empty.csv"
INVALID_TEST_CASE_1 = dir_path + "/sample_test_case/invalid_test_case1_extra_one_column_record.csv"
INVALID_TEST_CASE_2 = dir_path + "/sample_test_case/invalid_test_case2_missing_one_column_record.csv"
INVALID_TEST_CASE_3 = dir_path + "/sample_test_case/invalid_test_case3_invalid_salary.csv"
INVALID_TEST_CASE_4 = dir_path + "/sample_test_case/invalid_test_case4_negative_salary.csv"
INVALID_TEST_EMPTY_FILE = dir_path + "/sample_test_case/invalid_test_empty_file.csv"
INVALID_DUPLICATE_ID_LOGIN = dir_path + "/sample_test_case/invalid_test_case_duplicate_id_login.csv"


def get_files(file_name):
    return {
        'file': (file_name, open(file_name, 'rb'), 'text/csv')
    }


def test_api_valid_test_case_1():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(VALID_TEST_CASE_1), verify=False)
    assert ret.status_code == HTTP_SUCCESS_STATUS
    assert ret.json()["message"] == SUCCESS_MSG_RESPONSE


def test_api_valid_test_case_2():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(VALID_TEST_CASE_2), verify=False)
    assert ret.status_code == HTTP_SUCCESS_STATUS
    assert ret.json()["message"] == SUCCESS_MSG_RESPONSE


def test_api_valid_test_case_3():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(VALID_TEST_CASE_3), verify=False)
    assert ret.status_code == HTTP_SUCCESS_STATUS
    assert ret.json()["message"] == SUCCESS_MSG_RESPONSE


def test_api_invalid_test_case_1():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(INVALID_TEST_CASE_1), verify=False)
    assert ret.status_code == HTTP_FAIL_STATUS
    assert ret.json()["message"] == FAIL_VALIDATION_FAIL


def test_api_invalid_test_case_2():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(INVALID_TEST_CASE_2), verify=False)
    assert ret.status_code == HTTP_FAIL_STATUS
    assert ret.json()["message"] == FAIL_VALIDATION_FAIL


def test_api_invalid_test_case_3():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(INVALID_TEST_CASE_3), verify=False)
    assert ret.status_code == HTTP_FAIL_STATUS
    assert ret.json()["message"] == FAIL_VALIDATION_FAIL


def test_api_invalid_duplicate_login():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(INVALID_TEST_CASE_4), verify=False)
    assert ret.status_code == HTTP_FAIL_STATUS
    assert ret.json()["message"] == FAIL_VALIDATION_FAIL


def test_api_invalid_empty_file():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(INVALID_TEST_EMPTY_FILE), verify=False)
    assert ret.status_code == HTTP_FAIL_STATUS
    assert ret.json()["message"] == FAIL_VALIDATION_FAIL


def test_api_invalid_duplicate_id_login():
    ret = requests.post(FILE_UPLOAD_URL, headers=HEADERS, files=get_files(INVALID_DUPLICATE_ID_LOGIN), verify=False)
    assert ret.status_code == HTTP_FAIL_STATUS
    assert ret.json()["message"] == FAIL_VALIDATION_FAIL
