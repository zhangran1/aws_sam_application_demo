import sys
import os
import logging
from pathlib import Path
from datetime import datetime
import psycopg2
from psycopg2 import sql

sys.path.append(str(Path.cwd()))

from apps import db_config
from tests.unit import test_constants

logger = logging.getLogger()

DB_LOCK_ID = db_config.database_lock_id
TEST_LOCK = test_constants.SAMPLE_LOCK_ID


def make_connection(endpoint="localhost",
                    data_base=db_config.database,
                    db_user=db_config.db_user,
                    db_password=db_config.password,
                    db_port=db_config.port):
    """Connection function to establish database connection. During development, the connection information will be
       hard coded, however during actual deployment to AWS, the connection information will be retrieved from
       other services eg aws secret manager etc.

    Returns:
        Postgrest connection.
    """
    conn_str = "host={0} dbname={1} user={2} password={3} port={4}".format(endpoint,
                                                                           data_base,
                                                                           db_user,
                                                                           db_password,
                                                                           db_port)
    conn = psycopg2.connect(conn_str)
    conn.set_client_encoding('UTF8')
    conn.autocommit = True
    return conn


def init_lock_table():
    """
    Due to time constrain, this is purely hard code

    """
    try:

        cnx = make_connection()
        cursor = cnx.cursor()

        test_lock_query = ("INSERT INTO public.db_lock(lock_status, lock_id) VALUES(DEFAULT, %s)")
        actual_lock_query = ("INSERT INTO public.db_lock(lock_status, lock_id) VALUES(DEFAULT, %s)")

        cursor.execute(test_lock_query, (TEST_LOCK,))
        cursor.execute(actual_lock_query, (DB_LOCK_ID,))

        return False

    except Exception as e:
        logger.error(e)
        logger.error("Failed to update Record")
        return True
    finally:
        try:
            cnx.close()
        except:
            pass


if __name__ == "__main__":
    """
    This method is due to out of time, the proper way shall be use database inject to update value which can be done 
    directly from docker init. This is not common way to update database which is not preferred
    """
    init_lock_table()
