import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    type1_patients = patients[patients['conditions'].str.contains(r'\bDIAB1')==True]
    return type1_patients
    
