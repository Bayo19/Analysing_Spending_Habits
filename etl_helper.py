# transform functions

def delete_column(row, *args):
    for arg in args:
        del row[arg]
        
def str_to_float(row, *args):
    for arg in args:
        try:
            row[arg] = float(row[arg])
        except ValueError:
            row[arg] = row[arg]
            
def remove_credit_transactions(dataset):
    return [row for row in dataset if len(row['Debit Amount']) !=0]