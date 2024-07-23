import oracledb
from oracledb.connection import Connection
from typing import Dict, Union

connection: Connection
constants: Dict[str, Dict[int, str]]

def connect_db():
    global connection
    
    username = 'sharif'
    password = 'bish$12345'
    dsn = f'//192.168.234.76:2483/deva'

    try:
        oracledb.init_oracle_client(lib_dir='D:\\instantclient_19_23')
        connection = oracledb.connect(user=username, password=password, dsn=dsn)
        print("Successfully connected to Oracle database!\n")
    except oracledb.Error as error:
        print("Connection error:", error)

def query(query_str: str):
    print(query_str)
    cur = connection.cursor()
    try:
        cur.execute(query_str)
    finally:
        connection.commit()

def select_query(query_str: str):
    print(query_str)
    try:
        with connection.cursor() as cur:
            return list(cur.execute(query_str))
    finally:
        connection.commit()

def initialize_constants():
    global constants
    constants = {'marital_status': {},
                 'gender': {},
                 'emp_position': {},
                 'department': {},
                 'edu_level': {},
                 'edu_prog': {},
                 'timesheet_type': {}}
    for table in constants.keys():
        for elem in select_query(f'select * from {table}'):
            constants[table][elem[0]] = elem[1]

def find_constant_key(table_name, value):
    return [k for k, v in constants[table_name].items() if v == value][0]