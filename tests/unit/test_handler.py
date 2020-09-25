import sys
import json

from apps import upload
from tests.unit.test_cases import *

sys.path.append('././apps/')


def test_user_input_valid_test_case_1(user_input_valid_test_case_1, mocker):
    ret = upload.lambda_handler(user_input_valid_test_case_1, "")
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 200
