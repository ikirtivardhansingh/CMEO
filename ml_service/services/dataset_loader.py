import pandas as pd
from ml_service.services.validator import Validator
from ml_service.preprocessors.preprocessor import Preprocessor
class DatasetLoader:

    def load(self, file_path):
        return pd.read_csv(file_path)
    
loader = DatasetLoader()

df = loader.load("datasets/tcc.csv")

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


preprocessor = Preprocessor()

processed_data = preprocessor.process(
    df,
    target_column="Churn",
    drop_columns=["customerID"],
    binary_columns=[
        "Partner",
        "Dependents",
        "PaperlessBilling"
    ],
    categorical_columns=[
        "Contract"
    ],
    numerical_columns=[
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]
)

print(processed_data.keys())