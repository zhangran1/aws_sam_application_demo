import sys
import logging
import csv
import base64
import pytest

sys.path.append('././apps/')

from apps import multipart_form_parser as parser
from apps import employee
from tests.unit.test_constants import *

logger = logging.getLogger()


@pytest.fixture(scope="function")
def valid_upload_data_parser():
    logger.info("\n---------------setup valid upload data------------------")
    data = VALID_PROCESSED_DATA_TEST_CASE_1
    record = data[0]
    csv_data = csv.reader(record.splitlines(), delimiter=',')
    valid_upload_data_parser = parser.UploadDataParser(csv_data)
    yield valid_upload_data_parser
    logger.info("\n---------------tear down valid upload data------------------")


@pytest.fixture(scope="function")
def invalid_upload_data_parser():
    logger.info("\n---------------setup invalid upload data------------------")
    data = INVALID_EMPTY_FILE_PROCESSED_DATA
    record = data[0]
    csv_data = csv.reader(record.splitlines(), delimiter=',')
    invalid_upload_data_parser = parser.UploadDataParser(csv_data)
    yield invalid_upload_data_parser
    logger.info("\n---------------tear down invalid upload data------------------")


@pytest.fixture(scope="function")
def employee_object():
    logger.info("\n---------------setup new employee------------------")
    employee_object = employee.Employee("test00001", "john1", "John Smith", 100.5)
    yield employee_object
    logger.info("\n---------------tear down new employee------------------")
