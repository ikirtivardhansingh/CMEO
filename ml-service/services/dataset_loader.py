import pandas as pd

class DatasetLoader:

    def load(self, file_path):
        return pd.read_csv(file_path)
    
loader = DatasetLoader()

df = loader.load("datasets/WA_Fn-UseC_-Telco-Customer-Churn.csv")

print(df.head())
print(df.columns)