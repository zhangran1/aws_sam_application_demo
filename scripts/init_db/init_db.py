import logging

from datetime import datetime
import psycopg2
from psycopg2 import sql
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

        test_lock = ("INSERT INTO public.db_lock(lock_status, lock_id) VALUES(DEFAULT, '228b27e3-2a74-4849-9eba')" )
        actual_lock = ("INSERT INTO public.db_lock(lock_status, lock_id) VALUES(DEFAULT, '228b27e3-2a74-4849-9eba-57944c96b07b')")

        cursor.execute(test_lock)
        cursor.execute(actual_lock)



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
    directly from docker init. This is unusally way to update database which is not preferred
    """
    init_lock_table()

