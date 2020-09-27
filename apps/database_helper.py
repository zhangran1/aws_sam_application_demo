import logging

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


def check_existing_employee(employee_id):
    """Check whether a given employee_id exist in database or not

    Args:
        employee_id (String): Id of employee.

    Returns:
        Returns numerical value:
         1. 0: no existing record found
         2. 1: record exist for given employee_id
    """
    try:
        cnx = make_connection()
        cursor = cnx.cursor()

        sql_query = ("select count(development.employee.id) "
                     "from development.employee "
                     "where employee.id = %s")

        cursor.execute(sql_query, (employee_id,))

        employee_count = cursor.fetchall()[0][0]

        return employee_count


    except Exception as e:
        record_count = 0
        logger.error(e)
        logger.error("Failed to Retrieve record")
        return record_count
    finally:
        try:
            cnx.close()
        except:
            pass