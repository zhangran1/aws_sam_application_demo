import logging

logger = logging.getLogger()


class UploadDataParser:
    def __init__(self, multipart_form):
        self.multipart_form = list(multipart_form)
        self.row_count = len(self.multipart_form)
        self.valid_input = False

