import pandas as pd
from validator import Validator

class DatasetLoader:

    def load(self, file_path):
        return pd.read_csv(file_path)
    
loader = DatasetLoader()

df = loader.load("datasets/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())
print(df.columns)

validator = Validator()
validator.validate_not_empty(df)
validator.validate_target_column(
    df,
    "Churn"
)
validator.validate_required_columns(
    df,
    [
        "tenure",
        "MonthlyCharges",
        "Contract"
    ]
)

print("All validations passed")