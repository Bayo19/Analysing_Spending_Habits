import etl_helper as e_helper
import extract_transaction_details as extract


def transform(raw_dataset, list_to_read_to):
    dataset_without_credit_transactions = e_helper.remove_credit_transactions(raw_dataset)
    for row in dataset_without_credit_transactions:
        e_helper.delete_column(row, 'Account Number', 'Sort Code')
        e_helper.str_to_float(row, 'Debit Amount', 'Credit Amount', 'Balance')
        list_to_read_to.append(row)    

# extract_result = []
# extract.extract('15-16.csv', extract_result)


# transform_result = []
# transform(extract_result, transform_result)

# import pprint
# pprint.pprint(transform_result)
# print(len(transform_result))



