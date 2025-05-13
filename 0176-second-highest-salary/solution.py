import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee["rank"] = employee["salary"].rank(method="dense", ascending=False)
    second_highest = employee[employee["rank"]==2].iloc[:1]
    if second_highest.empty:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    else:
        return second_highest.rename(columns={"salary": "SecondHighestSalary"})[["SecondHighestSalary"]]
