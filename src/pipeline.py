import extract_transform_bank_transaction_details as extract_transform
import load_transaction_details as load

def pipeline(file_name):
    extract_result = []
    extract_transform.extract(file_name, extract_result)
    transform_result = []
    extract_transform.transform(extract_result, transform_result)
    
    connection = load.create_connection()
    load.create_transaction_description_table(connection)
    load.create_purchases_table(connection)
    load.create_processed_files_table(connection)
    
    for row in transform_result:
       load.insert_into_transaction_description_table(connection, row['Transaction Details'])
       td_id_foreign_key = load.get_td_id(row['Transaction Details'])
       load.insert_into_purchases_table(connection, td_id_foreign_key, row['Debit Amount'], row['Season'], row['Balance'])
       load.insert_into_processed_files_table(connection, file_name)
