import datetime

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

def get_month_from_date(date):
    dt = datetime.datetime.strptime(date, "%d/%m/%Y")
    month = dt.strftime('%B')
    return month
    
def get_season_from_month(month): 
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'

def add_new_key_value(row, key, value):
    row[key] = value

def delete_duplicates(arr):
    result = []
    for row in arr:
        if row not in result:
            result.append(row)
    return result
