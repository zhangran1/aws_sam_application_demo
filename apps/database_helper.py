import logging

from datetime import datetime
import pytz
import psycopg2

from db_config import *
from constants import *

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


def create_employee(employee_record):
    """Take in a Employee record. If the employee id exist in database, the existing record will be
       updated. If the existing employee id does not exist in database, a new record will be created
    Args:
        employee_record (Employee): Single Employee records to be created or updated.

    Returns:
        Returns response message to indicate the status of database operation:
         1. DB_FAILED_OPERATION: Failed
         2. DB_SUCCESS_OPERATION: OK
    """
    try:
        employee_record_update = True
        cnx = make_connection()
        cursor = cnx.cursor()

        create_new_record = ("insert into development.employee(id, login, name, salary) "
                             "values (%s, %s, %s, %s)")

        update_existing_record = ("update development.employee set login = %s, name = %s, salary = %s where id = %s")

        new_record_details = ("insert into development.employ_create_details(created_at, employee_id) "
                              "values (%s, %s)")

        update_record_details = ("update development.employ_create_details set updated_at = %s where employee_id = %s")

        # todo concurrent update is not handled at the moment, to be implemented at later time
        record_count = check_existing_employee(employee_record.employee_id)
        current_time = str(datetime.now(pytz.timezone("Asia/Singapore")))
        if record_count == 1:

            cursor.execute(update_existing_record, (employee_record.login,
                                                    employee_record.name, employee_record.salary,
                                                    employee_record.employee_id))
            cursor.execute(update_record_details, (current_time, employee_record.employee_id))

        elif record_count == 0:
            cursor.execute(create_new_record, (employee_record.employee_id,
                                               employee_record.login,
                                               employee_record.name,
                                               employee_record.salary))

            cursor.execute(new_record_details, (current_time, employee_record.employee_id))

        # todo check whether the above operation performed successfully
        # can be done by via row count, or other postgres built in messages

        return DB_SUCCESS_OPERATION

    except Exception as e:
        logger.error(e)
        logger.error("Failed to update Record")
        return DB_FAILED_OPERATION
    finally:
        try:
            cnx.close()
        except:
            pass


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


def check_db_lock(db_lock_id=database_lock_id):
    """Check is there any file upload process being in place

    Returns:
        Returns boolean value:
        True:  Upload is in progress
        False: No upload is taking in place
    """
    try:
        cnx = make_connection()
        cursor = cnx.cursor()

        db_lock_query = ("select development.db_lock.lock_status from development.db_lock where db_lock.lock_id = %s")

        cursor.execute(db_lock_query, (db_lock_id, ))
        # todo check whether the above operation performed successfully
        # can be done by via row count, or other postgres built in messages

        db_lock_status = cursor.fetchall()
        logger.info(db_lock_status[0][0])

        return db_lock_status[0][0]

    except Exception as e:
        db_lock_status = True
        logger.error(e)
        logger.error("Failed to get the lock")
        return db_lock_status
    finally:
        try:
            cnx.close()
        except:
            pass


def get_db_lock(db_lock_id=database_lock_id):
    """Get db lock for user file upload.

    Returns:
        Returns boolean value:
         1. DB_FAILED_OPERATION: Failed
         2. DB_SUCCESS_OPERATION: OK
    """
    try:
        cnx = make_connection()
        cursor = cnx.cursor()

        get_db_lock = ("update development.db_lock set lock_status = True where lock_id = %s")

        cursor.execute(get_db_lock, (db_lock_id, ))
        # todo check whether the above operation performed successfully
        # can be done by via row count, or other postgres built in messages

        return DB_SUCCESS_OPERATION

    except Exception as e:
        logger.error(e)
        logger.error("Failed to get the lock")
        return DB_FAILED_OPERATION
    finally:
        try:
            cnx.close()
        except:
            pass


def release_db_lock(db_lock_id=database_lock_id):
    """Release db lock for user file upload.

    Returns:
        Returns boolean value:
         1. DB_FAILED_OPERATION: Failed
         2. DB_SUCCESS_OPERATION: OK
    """
    try:
        cnx = make_connection()
        cursor = cnx.cursor()

        get_db_lock = ("update development.db_lock set lock_status = False where lock_id = %s")

        cursor.execute(get_db_lock, (db_lock_id, ))
        # todo check whether the above operation performed successfully
        # can be done by via row count, or other postgres built in messages

        return DB_SUCCESS_OPERATION

    except Exception as e:
        logger.error(e)
        logger.error("Failed to get the lock")
        return DB_FAILED_OPERATION
    finally:
        try:
            cnx.close()
        except:
            pass