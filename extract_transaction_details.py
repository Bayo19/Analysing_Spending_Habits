import csv
                
def extract(file, list_to_append_to):
    with open(file, 'r') as file_name:
        for row in csv.DictReader(file_name):
            list_to_append_to.append(row)



# Tables to make
# transaction description (id, td_name)
# credit - (td_id, amount received)
# debit - (td_id, amount spent, percentage of current balance)

# objective of this task is to find out which places/people have been getting the most of my money and to also observe and do something about my spending habits

