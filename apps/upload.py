import os
import json
import logging


logger = logging.getLogger()
logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-6s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%Y-%m-%d:%H:%M:%S',
                    level=os.environ.get("LOGLEVEL", "INFO"))

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

    context: object, required
        Lambda Context runtime methods and attributes

    Returns
    ------

    """


    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "File uploaded successfully",
        }),
    }
