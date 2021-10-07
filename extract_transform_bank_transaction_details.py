import csv
import etl_helper as e_helper
            
def extract(file, list_to_append_to):
    with open(file, 'r') as file_name:
        for row in csv.DictReader(file_name):
            list_to_append_to.append(row)


def transform(raw_dataset, list_to_read_to):
    
    dataset_without_credit_transactions = e_helper.remove_credit_transactions(raw_dataset)
    
    for row in dataset_without_credit_transactions:
        e_helper.delete_column(row, 'Account Number', 'Credit Amount', 'Sort Code')
        e_helper.str_to_float(row, 'Balance', 'Debit Amount')
        
        month = e_helper.get_month_from_date(row['Transaction Date'])
        season_of_year = e_helper.get_season_from_month(month)
        
        e_helper.add_new_key_value(row, 'Season', season_of_year)
        list_to_read_to.append(row)    

extract_result = []
extract('csv_files/15-16.csv', extract_result)
transform_result = []
transform(extract_result, transform_result)

import pprint as p
p.pprint(transform_result[0])
