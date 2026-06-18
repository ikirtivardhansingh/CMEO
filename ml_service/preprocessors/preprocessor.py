from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd

class Preprocessor:

    def preprocessor(self, df, target_column, drop_columns):
        df = df.drop(columns = drop_columns)

        x = df.drop(columns = [target_column])
        y = df[target_column]

        return x, y
    
    def encode_binary_columns(self, df, binary_columns):
        for column in binary_columns:
            df[column] = df[column].map({
                "Yes": 1,
                "No" : 0
            })
        return df
    def encode_categorical_columns(
            self, 
            df, 
            categorical_columns
    ):
        for column in categorical_columns:
            df[column] = df[column].astype("category").cat.codes
        return df
    
    def scale_numerical_columns(
        self,
        df,
        numerical_columns
    ):
        scaler = MinMaxScaler()
        df[numerical_columns] = scaler.fit_transform(
            df[numerical_columns]
        )
       
        return df
    def split_data(
            self,
            X,
            y,
            test_size = 0.2
    ):
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=42
        )
        return (
            X_train,
            X_test,
            y_train,
            y_test
        )
    
    
    def process(
            self,
            df,
            target_column,
            drop_columns,
            binary_columns,
            categorical_columns,
            numerical_columns,
            selected_features
    ):
        
        df = df.drop(columns = drop_columns)
        df = self.encode_binary_columns(
            df,
            binary_columns
        )

        df = self.encode_categorical_columns(
            df,
            categorical_columns
        )


        df = self.encode_categorical_columns(
            df,
            categorical_columns
        )
        df = self.handle_missing_values(df)
        df = self.scale_numerical_columns(
            df, 
            numerical_columns
        )
        df = df[selected_features + [target_column]]
    
        x = df.drop(columns=[target_column])
        print(x.columns)
        y = df[target_column]

        (
            X_train,
            X_test,
            y_train,
            y_test
        ) = self.split_data(x, y)

        return {
            "X_train": X_train,
            "X_test": X_test,
            "y_train": y_train,
            "y_test": y_test
        }
    
    def handle_missing_values(
    self,
    df
    ):
   
        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"],
            errors="coerce"
        )

   
        df["TotalCharges"] = df["TotalCharges"].fillna(0)

        return df


    


        
