import datetime

# transform functions

def delete_column(row, *args):
    for arg in args:
        del row[arg]
    return row # may need to remove return

      
def str_to_float(row, *args):
    for arg in args:
        try:
            row[arg] = float(row[arg])
        except ValueError:
            row[arg] = row[arg]

            
def remove_credit_transactions(dataset):
    return [row for row in dataset if len(row['Debit Amount']) !=0]


def get_month_from_date(date):
    dt = datetime.datetime.strptime(date, "%d/%m/%Y")
    month = dt.strftime('%B')
    return month

    
def get_season_from_month(month): 
    if month in {'December', 'January', 'February'}:
        return 'Winter'
    elif month in {'March', 'April', 'May'}:
        return 'Spring'
    elif month in {'June', 'July', 'August'}:
        return 'Summer'
    elif month in {'September', 'October', 'November'}:
        return 'Autumn'


def add_new_key_value(row, key, value):
    row[key] = value


def delete_duplicates(arr):
    unique_result = []
    [unique_result.append(row) for row in arr if row not in unique_result]
    return(unique_result)


def format_date_postgres(date): 
    dt = datetime.datetime.strptime(date, "%d/%m/%Y")
    new_date = dt.strftime('%m/%d/%Y')
    return new_date

# file processing functions

def run_pipeline(file_set, filename, fn):
    if filename not in file_set:
        fn(filename)
