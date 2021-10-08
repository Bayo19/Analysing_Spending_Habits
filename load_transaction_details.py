import psycopg2

def create_connection():
    conn = psycopg2.connect(
        user='root',
        password='password',
        host='localhost',
        database='my_transactions',
        port=5438
    )
    return conn

connection = create_connection()

def close_connection(cur):
    cur.close()

def execute_command(connection, command, values=None):
    cur = connection.cursor()
    cur.execute(command)
    connection.commit()
    close_connection(cur)


def create_transaction_description_table(con):
    command = '''CREATE TABLE if not exists transaction_descriptions(
                td_id SERIAL,
                td_name VARCHAR (255) NOT NULL,
                PRIMARY KEY(td_id))'''
                
    execute_command(con, command)

def create_purchases_table(con):
    command = '''CREATE TABLE if not exists purchases(
                purchases_id SERIAL,
                td_id INT NOT NULL,
                amount_spent FLOAT(2) NOT NULL, 
                season VARCHAR(255) NOT NULL, 
                balance FLOAT(2) NOT NULL,
                PRIMARY KEY(purchases_id),
                FOREIGN KEY(td_id) REFERENCES transaction_descriptions(td_id))'''
    execute_command(con, command)
    
def create_processed_files_table(con):
    command = '''CREATE TABLE if not exists processed_files(
                file_id SERIAL,
                file_name VARCHAR(255) NOT NULL)'''
    execute_command(con, command)


create_transaction_description_table(connection)
create_purchases_table(connection)
create_processed_files_table(connection)

def insert_into_transaction_description_table(con, td_name):
    pass
def insert_into_purchases_table(con, td_id, amount_spent, season, balance):
    pass
def insert_into_processed_files_table(con, file_name):
    pass

