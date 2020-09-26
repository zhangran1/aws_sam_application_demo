import csv
import base64


def filter_csv_data(multi_form_data):
    """Process event body input and return processed data.
    Original raw data format for multi-format data:
        --------------------123456789
        data content one
        --------------------123456789
        data content two
        --------------------123456789
    After split the data, list of record will be returned
        [data content one, data content two]

    Args:
        multi_form_data (string): Even body.

    Returns:
        Json response contains the following fields:
        0. status: failed.
        1. statusCode: 400 (Client side error)
        2. body: Json data contains return message.

    """
    post_data = base64.b64decode(multi_form_data)
    headers, data = post_data.decode('utf-8').split('\r\n', 1)
    data = data.split(headers)
    return data
