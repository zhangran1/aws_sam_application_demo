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


@pytest.fixture(scope="function")
def valid_employee_records():
    logger.info("\n---------------setup new employee------------------")
    valid_employee_records = []
    employee_john1 = employee.Employee("test00001", "john1", "John Smith", 101.5)
    employee_john2 = employee.Employee("test00002", "john2", "John Smith2", 102.5)
    employee_john3 = employee.Employee("test00003", "john3", "John Smith3", 103.5)
    employee_john4 = employee.Employee("test00004", "john4", "John Smith4", 104.5)
    employee_john5 = employee.Employee("test00005", "john5", "John Smith5", 105.5)
    employee_john6 = employee.Employee("test00006", "john6", "John Smith6", 106.5)
    employee_john7 = employee.Employee("test00007", "john7", "John Smith7", 107.5)
    employee_john8 = employee.Employee("test00008", "john8", "John Smith8", 108.5)
    employee_john9 = employee.Employee("test00009", "john9", "John Smith9", 109.5)
    employee_john10 = employee.Employee("test000010", "john10", "John Smith10", 110.5)
    employee_adam1 = employee.Employee("test000011", "adam1", "Adam1", 1001.5)
    employee_adam2 = employee.Employee("test000012", "adam2", "Adam2", 1002.5)
    employee_adam3 = employee.Employee("test000013", "adam3", "Adam3", 1003.5)
    employee_adam4 = employee.Employee("test000014", "adam4", "Adam4", 1004.5)
    employee_adam5 = employee.Employee("test000015", "adam5", "Adam5", 30.5)
    valid_employee_records.append(employee_john1)
    valid_employee_records.append(employee_john2)
    valid_employee_records.append(employee_john3)
    valid_employee_records.append(employee_john4)
    valid_employee_records.append(employee_john5)
    valid_employee_records.append(employee_john6)
    valid_employee_records.append(employee_john7)
    valid_employee_records.append(employee_john8)
    valid_employee_records.append(employee_john9)
    valid_employee_records.append(employee_john10)
    valid_employee_records.append(employee_adam1)
    valid_employee_records.append(employee_adam2)
    valid_employee_records.append(employee_adam3)
    valid_employee_records.append(employee_adam4)
    valid_employee_records.append(employee_adam5)

    yield valid_employee_records

    logger.info("\n---------------tear down new employee------------------")