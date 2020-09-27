import logging
import decimal
import constants
import employee
logger = logging.getLogger()


class UploadDataParser:
    def __init__(self, multipart_form):
        self.multipart_form = list(multipart_form)
        self.row_count = len(self.multipart_form)
        self.valid_input = False
        self.processed_employee_record = []
        self.employee_record = []
        self.__filter_data()

    def __filter_data(self):
        if not self.multipart_form[0]:
            self.multipart_form = self.multipart_form[1:-1]

        form_data = self.multipart_form[0][0]
        form_data = form_data.split(";")

        self.__validate_empty_file(form_data)

        if self.valid_input:
            self.__line_validation(self.multipart_form[4:])


    def __validate_empty_file(self, form_data):
        for item in form_data:
            item = item.lstrip().replace("=", ":").split(":")
            if item[0] == "name" and (item[1] == "file" or item[1] == '"file"'):
                if self.row_count > constants.MINIMUM_ROW_COUNT:
                    self.valid_input = True

    def __line_validation(self, csv_data):

        for row_item in csv_data:
            # any actual content line start with # will be ommitted

            # cater for the case last line is empty
            if len(row_item) == 0:
                continue

            if row_item[0].startswith("#"):
                continue

            # only four items are allowed per row record
            if len(row_item) != constants.VALID_LINE_INPUT:
                self.valid_input = False
                break

            # salary should be decimal value
            try:
                decimal.Decimal(row_item[3])
            except decimal.InvalidOperation:
                self.valid_input = False
                break

            # salary should be more than 0
            if decimal.Decimal(row_item[3]) < 0:
                self.valid_input = False
                break

            employee_id = row_item[0]
            login = row_item[1]
            name = row_item[2]
            salary = decimal.Decimal(row_item[3])

            recorded_item = {
                employee_id: login
            }
            if recorded_item not in self.processed_employee_record:
                self.processed_employee_record.append(recorded_item)
            else:
                self.valid_input = False
                break

            employee_record = employee.Employee(employee_id, login, name, salary)
            self.employee_record.append(employee_record)






