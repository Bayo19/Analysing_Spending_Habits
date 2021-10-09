import src.load_transaction_details as load

connection = load.create_connection()

def select_all_file_names(con):
    command = '''SELECT file_name FROM processed_files'''
    cur = con.cursor()
    cur.execute(command)
    record = cur.fetchall()
    cur.close()
    return {i[0] for i in record}

processed_files_list = select_all_file_names(connection)

def run_pipeline(file_set, filename, fn):
    if filename not in file_set:
        fn(filename)
