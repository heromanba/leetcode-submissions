import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    mask1 = insurance.groupby('tiv_2015')['pid'].transform("count") > 1
    mask2 = insurance.groupby(['lat', 'lon'])['pid'].transform("count") == 1
    ret = insurance[mask1&mask2]['tiv_2016'].sum()
    return pd.DataFrame({"tiv_2016": [ret]})
    
