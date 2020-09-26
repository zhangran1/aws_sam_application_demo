import os
import json
import logging
import uuid
import traceback

from datetime import datetime
import pytz
import psycopg2

from db_config import *

logger = logging.getLogger()

def make_connection():
    """Connection function to establish database connection. During development, the connection information will be
       hard coded, however during actual deployment to AWS, the connection information will be retrieved from
       other services eg aws secret manager etc.

    Returns:
        Postgrest connection.
    """
    conn_str = "host={0} dbname={1} user={2} password={3} port={4}".format(endpoint, database, db_user, password, port)
    conn = psycopg2.connect(conn_str)
    conn.autocommit = True
    return conn

