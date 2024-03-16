import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, left_on = 'id', right_on = 'customerId', how = 'left', suffixes = ('_customer','_order'))
    return df[df['customerId'].isnull() == True][['name']].rename(columns={'name':'customers'})
