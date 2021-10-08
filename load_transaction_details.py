import psycopg2

def create_database():
    con = psycopg2.connect(
    user="root",
    password="password",
    host="localhost",
    port=5438)

    cur = con.cursor()
    con.autocommit = True
    cur.execute('create database my_transactions')
    cur.close()
    con.close()

def create_connection():
    conn = psycopg2.connect(
        user='root',
        password='password',
        host='localhost',
        database='my_transactions',
        port=5438
    )
    return conn

def close_connection(cur):
    cur.close()

def execute_command(connection, command, values=None):
    val = (values,)
    cur = connection.cursor()
    cur.execute(command, val)
    connection.commit()
    close_connection(cur)

def create_transaction_description_table(con):
    command = '''CREATE TABLE if not exists transaction_descriptions(
                td_id SERIAL,
                td_name VARCHAR (255) UNIQUE NOT NULL ,
                PRIMARY KEY(td_id))'''
                
    execute_command(con, command)

def create_purchases_table(con):
    command = '''CREATE TABLE if not exists purchases(
                purchases_id SERIAL,
                td_id INT NOT NULL,
                amount_spent FLOAT(2) NOT NULL, 
                season VARCHAR(255) NOT NULL, 
                balance FLOAT(2) NOT NULL,
                PRIMARY KEY(purchases_id, td_id, amount_spent, balance),
                FOREIGN KEY(td_id) REFERENCES transaction_descriptions(td_id))'''
    execute_command(con, command)
    
def create_processed_files_table(con):
    command = '''CREATE TABLE if not exists processed_files(
                file_id SERIAL,
                file_name VARCHAR(255) NOT NULL,
                PRIMARY KEY(file_id))'''
    execute_command(con, command)

try:
    create_database()
except:
    pass

connection = create_connection()
create_transaction_description_table(connection)
create_purchases_table(connection)
create_processed_files_table(connection)

def insert_into_transaction_description_table(con, values):
    command = '''INSERT INTO transaction_descriptions (td_name)
                VALUES (%s)
                ON CONFLICT (td_name)
                DO NOTHING'''
                
    execute_command(con, command, values)

def insert_into_purchases_table(con, td_id, amount_spent, season, balance):
    command = '''INSERT INTO purchases (td_id, amount_spent, season, balance)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (amount_spent, season, balance)
                DO NOTHING'''


def insert_into_processed_files_table(con, values):
    command = '''INSERT INTO processed_files (file_name)
                VALUES (%s)
                ON CONFLICT (file_name)
                DO NOTHING'''
                
    execute_command(con, command, values)
    

def get_td_id(con, transaction_name):

    command = f'SELECT td_id FROM transaction_descriptions WHERE td_name = %s'
    cur = con.cursor()
    val = (transaction_name,)
    cur.execute(command,val)
    record = cur.fetchall()
    cur.close()
    return record[0][0]




