import csv
import etl_helper as e_helper
            
def extract(file, list_to_append_to):
    with open(file, 'r') as file_name:
        for row in csv.DictReader(file_name):
            list_to_append_to.append(row)


def transform(raw_dataset, list_to_read_to):
    
    dataset_without_credit_transactions = e_helper.remove_credit_transactions(raw_dataset)
    
    for row in dataset_without_credit_transactions:
        new_row = e_helper.remove_key_with_empty_value(row, 'Credit Amount')
        e_helper.delete_column(new_row, 'Account Number', 'Sort Code')
        e_helper.str_to_float(new_row, 'Debit Amount', 'Balance')
        list_to_read_to.append(new_row)    


# Tables to make
# transaction description (id, td_name)
# debit - (td_id, amount spent, percentage of current balance)

# objective of this task is to find out which places/people have been getting the most of my money and to also observe and do something about my spending habits

