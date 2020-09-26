import sys
import logging
import pytest

sys.path.append('././apps/')

from apps import multipart_form_parser as parser
from tests.unit.test_constants import *

logger = logging.getLogger()


@pytest.fixture(scope="function")
def upload_data_parser():
    logger.info("\n---------------setup------------------")
    upload_data_parser = parser.UploadDataParser(VALID_PROCESSED_DATA_TEST_CASE_1)
    yield upload_data_parser
    logger.info("\n---------------tear down------------------")
