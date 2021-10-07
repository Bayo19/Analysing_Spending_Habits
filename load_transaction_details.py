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
                td_id SERIAL(Primary Key),
                td_name VARCHAR (255) NOT NULL)'''
                
    execute_command(con, command)

def create_purchases_table(con):
    command = '''CREATE TABLE if not exists purchases(
                purchases_id(Primary Key),
                td_id SERIAL,
                amount_spent, season, percentage of current balance
    )
    '''

create_transaction_description_table(connection)