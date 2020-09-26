import sys
import json

from apps import upload
from tests.unit.test_cases import *
from tests.unit.test_constants import *


sys.path.append('././apps/')



def test_user_input_valid_test_case_1(user_input_valid_test_case_1, mocker):
    ret = upload.lambda_handler(user_input_valid_test_case_1, "")
    data = json.loads(ret["body"])
    assert data["message"] == SUCCESS_MSG_RESPONSE
    assert ret["statusCode"] == HTTP_SUCCESS_STATUS


def test_user_input_valid_test_case_2(user_input_valid_test_case_2, mocker):
    ret = upload.lambda_handler(user_input_valid_test_case_2, "")
    data = json.loads(ret["body"])
    assert data["message"] == SUCCESS_MSG_RESPONSE
    assert ret["statusCode"] == HTTP_SUCCESS_STATUS


def test_user_input_invalid_test_case_1(user_input_invalid_test_case_1, mocker):
    ret = upload.lambda_handler(user_input_invalid_test_case_1, "")
    data = json.loads(ret["body"])
    assert data["message"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_case_2(user_input_invalid_test_case_2, mocker):
    ret = upload.lambda_handler(user_input_invalid_test_case_2, "")
    data = json.loads(ret["body"])
    assert data["message"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_user_input_invalid_test_case_3(user_input_invalid_test_case_3, mocker):
    ret = upload.lambda_handler(user_input_invalid_test_case_3, "")
    data = json.loads(ret["body"])
    assert data["message"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS


def test_invalid_test_empty_file(invalid_test_empty_file, mocker):
    ret = upload.lambda_handler(invalid_test_empty_file, "")
    data = json.loads(ret["body"])
    assert data["message"] == FAIL_VALIDATION_FAIL
    assert ret["statusCode"] == HTTP_FAIL_STATUS

