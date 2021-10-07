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


# Tables to make
# transaction description (id, td_name)
# purchases- (td_id, amount spent, season, percentage of current balance)

# objective of this task is to find out which places/people have been getting the most of my money and to also observe and do something about my spending habits

# add season to each row so that we can group by season later in sql

# THINGS TO ANALYZE

# .day in week where I spend the most money
# .season where I spend the most money
# .average amount of money spent per month over the years
# .places where I spent the most money
# .places where I shopped the most
