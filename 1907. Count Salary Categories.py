import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame()
    result['category'] = ['Low Salary','Average Salary','High Salary']
    result['accounts_count'] = [
        (accounts['income'] < 20000).sum(),
        ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum(),
        (accounts['income'] > 50000).sum()
    ]
    return result
