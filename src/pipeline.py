import extract_transform_bank_transaction_details as extract_transform
import SQL_funcs as load

def pipeline(file_path):
    extract_result = []
    extract_transform.extract(file_path, extract_result)
    transform_result = []
    extract_transform.transform(extract_result, transform_result)
    
    connection = load.create_connection()
    
    load.create_transaction_description_table(connection)
    load.create_purchases_table(connection)
    load.create_processed_files_table(connection)
    
    for row in transform_result:
       load.insert_into_transaction_description_table(connection, row['Transaction Description'])
       td_id_foreign_key = load.get_td_id(connection, row['Transaction Description'])
       load.insert_into_purchases_table(connection, td_id_foreign_key, row['Debit Amount'], row['Season'], row['Transaction Date'], row['Balance'])
       load.insert_into_processed_files_table(connection, file_path)

    print(f'{file_path}: processing complete')
