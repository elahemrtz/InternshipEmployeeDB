import oracledb
from oracledb.connection import Connection
from typing import Dict

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
    cur = connection.cursor()
    return cur.execute(query_str)

def initialize_constants():
    global constants
    constants = {'marital_status': {},
                 'gender': {},
                 'emp_position': {},
                 'department': {},
                 'edu_level': {},
                 'edu_prog': {}}
    for table in constants.keys():
        for elem in query(f'select * from {table}'):
            constants[table][elem[0]] = elem[1]