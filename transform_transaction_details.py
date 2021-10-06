import etl_helper as e_helper
import extract_transaction_details as extract

def transform(raw_dataset, list_to_read_to):
    dataset_without_credit_transactions = e_helper.remove_credit_transactions(raw_dataset)
    for row in dataset_without_credit_transactions:
        new_row = e_helper.remove_key_with_empty_value(row, 'Credit Amount')
        e_helper.delete_column(new_row, 'Account Number', 'Sort Code')
        e_helper.str_to_float(new_row, 'Debit Amount', 'Balance')
        list_to_read_to.append(new_row)    




