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

def execute_command(connection, command):
    cur = connection.cursor()
    cur.execute(command)
    connection.commit()
    close_connection(cur)


def create_transaction_description_table(con):
    command = '''CREATE TABLE if not exists transaction_descriptions(
                td_id SERIAL,
                td_name VARCHAR (255) NOT NULL)'''
                
    execute_command(con, command)

def create_purchases_table(con):
    command = '''CREATE TABLE if not exists purchases(
                purchases_id,
                td_id SERIAL NOT NULL,
                amount_spent FLOAT(2) NOT NULL, 
                season VARCHAR(255) NOT NULL, 
                balance FLOAT(2))'''
    execute_command(con, command)
    
def create_processed_files(con):
    command = '''CREATE TABLE if not exists processed_files(
                file_id SERIAL NOT NULL,
                file_name VARCHAR(255) NOT NULL)'''
    execute_command(con, command)

create_transaction_description_table(connection)
create_purchases_table(connection)
create_processed_files(connection)