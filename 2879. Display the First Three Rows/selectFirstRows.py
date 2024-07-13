import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
        employees = employees.head(3)
        return employees 