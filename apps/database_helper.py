# -*- coding: utf-8 -*-

import logging
from datetime import datetime
import pytz
import psycopg2
import http_responses

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
    conn.set_client_encoding('UTF8')
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

        create_new_record = ("insert into public.employee(id, login, name, salary) "
                             "values (%s, %s, %s, %s)")

        update_existing_record = ("update public.employee set login = %s, name = %s, salary = %s where id = %s")

        new_record_details = ("insert into public.employ_create_details(created_at, employee_id) "
                              "values (%s, %s)")

        update_record_details = ("update public.employ_create_details set updated_at = %s where employee_id = %s")

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

        sql_query = ("select count(public.employee.id) "
                     "from public.employee "
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

        db_lock_query = ("select public.db_lock.lock_status from public.db_lock where db_lock.lock_id = %s")

        cursor.execute(db_lock_query, (db_lock_id,))
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

        get_db_lock = ("update public.db_lock set lock_status = True where lock_id = %s")

        cursor.execute(get_db_lock, (db_lock_id,))
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

        get_db_lock = ("update public.db_lock set lock_status = False where lock_id = %s")

        cursor.execute(get_db_lock, (db_lock_id,))
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


def retrieve_users_from_db(requested_params):
    """Retrieve employee records based on requested parameters. This function will only be invoke after validate
       requested_params.

        Args:
        requested_params (Dict): Request parameters include the following fields with restrictions:
                    1.minSalary: assume only take in integer minimum value is 0
                    2.maxSalary: integer
                    3.offset: integer minimum value is 0
                    4.limit: 1 to 30 integer value
                    5.sort: String start with "-" or "+", only can sort by "id", "name", "login", "salary"

        Json response contains the following fields:
         1. statusCode: 200 (OK), 400 (Client side error)
         2. body: Json data contains return message. If statusCode is 400, error message will be return.
                  If statusCode is 200, list of employee record will be stored in results
    """

    try:

        min_salary = int(requested_params["minSalary"])
        max_salary = int(requested_params["maxSalary"])
        offset = int(requested_params["offset"])
        limit = int(requested_params["limit"])
        sort_direction = requested_params["sort"][0]

        if sort_direction == "-":
            sort_direction = "desc"
        else:
            sort_direction = "asc"

        sort_by = "employee." + requested_params["sort"][1:]

        retrieve_employee_query = ("select public.employee.id, public.employee.login, " \
                                   "public.employee.name, public.employee.salary " \
                                   "from public.employee " \
                                   "inner join public.employ_create_details " \
                                   "on employee.id = employ_create_details.employee_id " \
                                   "where employ_create_details.delete_status = FALSE " \
                                   "and employee.salary > {min_salary} " \
                                   "and employee.salary < {max_salary} " \
                                   "order by {sort_by} {sort_direction}  " \
                                   "limit {limit} offset {offset}".format(min_salary=min_salary,
                                                                          max_salary=max_salary,
                                                                          sort_by=sort_by,
                                                                          sort_direction=sort_direction,
                                                                          limit=limit,
                                                                          offset=offset))

        cnx = make_connection()
        cursor = cnx.cursor()
        parameter = (min_salary, max_salary, limit, offset)
        cursor.execute(retrieve_employee_query)

        employee_records = cursor.fetchall()

        employee_response = []

        # todo update return data position
        for single_employee_record in employee_records:
            employee_record = {
                "id": single_employee_record[0],
                "login": single_employee_record[1],
                "name": single_employee_record[2],
                "salary": str(single_employee_record[3]),
            }
            employee_response.append(employee_record)

        cursor.close()
        # There might need to have one API to show total number of items belong to this user
        http_status = True
        return http_responses.http_standard_return(http_status, success_msg=employee_response)

    except Exception as e:
        logger.error(e)
        http_status = False
        return http_responses.http_standard_return(http_status, failed_msg=RETRIEVE_EMPLOYEE_FAILED)

    finally:
        try:
            cnx.close()
        except Exception as e:
            logging.exception(e)


def retrieve_user_record_by_id(user_id):
    """Retrieve employee records based on requested parameters. This function will only be invoke after validate
       requested_params.

        Args:
        user_id (String): Id of the user to be retreived

        Json response contains the following fields:
         1. statusCode: 200 (OK), 400 (User does not exist)
         2. body: Json data contains return message. If statusCode is 400, error message will be return.
                  If statusCode is 200, single employee record will be stored in results
    """

    try:

        retrieve_single_employee_query = ("select public.employee.name, public.employee.login, public.employee.salary "
                                          "from public.employee "
                                          "inner join public.employ_create_details "
                                          "on employee.id = employ_create_details.employee_id "
                                          "where employ_create_details.delete_status = FALSE "
                                          "and employee.id = %s")


        cnx = make_connection()
        cursor = cnx.cursor()

        cursor.execute(retrieve_single_employee_query, (user_id,))

        single_employee_record = cursor.fetchall()

        http_status = False

        if len(single_employee_record) == 0:
            return http_responses.http_standard_return(http_status, failed_msg=RETRIEVE_EMPLOYEE_FAILED)

        http_status = True
        employee_record = {
            "id": user_id,
            "name": single_employee_record[0][0],
            "login": single_employee_record[0][1],
            "salary": str(single_employee_record[0][2]),
        }

        cursor.close()
        # There might need to have one API to show total number of items belong to this user

        return http_responses.http_standard_return(http_status, success_msg=employee_record)

    except Exception as e:
        logger.error(e)
        http_status = False
        return http_responses.http_standard_return(http_status, failed_msg=RETRIEVE_EMPLOYEE_FAILED)

    finally:
        try:
            cnx.close()
        except Exception as e:
            logging.exception(e)


def db_real_delete_for_testing_purpose(user_id):
    """Physically employee records based on requested parameters. This function will really delete record for teseting
    purpose, use with care, as per the requirement, the delete function will not be physically delete the record.

        Args:
        user_id (String): Id of the user to be deleted

        Json response contains the following fields:
         1. statusCode: 200 (OK), 400 (User does not exist)
         2. body: Json data contains return message. If statusCode is 400, error message will be return.
                  If statusCode is 200, single employee record will be stored in results
    """

    try:

        physical_delete_for_testing_purpose = ("delete from public.employee where id = %s")

        cnx = make_connection()
        cursor = cnx.cursor()

        cursor.execute(physical_delete_for_testing_purpose, (user_id,))
        http_status = True

        cursor.close()

        return http_responses.http_standard_return(http_status)

    except Exception as e:
        logger.error(e)
        http_status = False
        return http_responses.http_standard_return(http_status, failed_msg=DB_FAILED_OPERATION)

    finally:
        try:
            cnx.close()
        except Exception as e:
            logging.exception(e)


def delete_employee(employee_id):
    """Take in employee id and delete the record. Only employee record delete will be updated to true, the data still
       keep in database
    Args:
        employee_id (String): Id of the employee.

    Returns:
        Returns response message to indicate the status of database operation:
         1. DB_FAILED_OPERATION: Failed
         2. DB_SUCCESS_OPERATION: OK
    """
    try:
        cnx = make_connection()
        cursor = cnx.cursor()

        # Assumption: Assume the id passed from api call is correct, strict checking shall be implemented depends on
        #  requirements
        current_time = str(datetime.now(pytz.timezone("Asia/Singapore")))
        delete_record = update_delete_record_details = ("update public.employ_create_details set "
                                                        "deleted_at = %s , delete_status = True "
                                                        "where employee_id = %s")

        cursor.execute(delete_record, (current_time, employee_id))
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
