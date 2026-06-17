class preprocessor:

    def preprocessor(self, df, target_column, drop_columns):
        df = df.drop(columns = drop_columns)

        x = df.drop(columns = [target_column])
        y = df[target_column]

        return x, y
    
    def encode_binary_colums(self, df, binary_columns):
        for column in binary_columns:
            df[column] = df[column].map({
                "yes": 1,
                "No" : 0
            })
        return df