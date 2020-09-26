import sys
import logging
import csv
import base64
import pytest

sys.path.append('././apps/')

from apps import multipart_form_parser as parser
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
