class Validator:
    
    def validate_taget_columns(self, df, target_column):
        if target_column not in df.columns:
            raise ValueError(
                f"Target column '{target_column}' not found in dataset"
            )
        
        return True
    
    def validate_not_empty(self, df):
        if df.empty: 
            raise ValueError(
                "Dataset is empty"
            )
        
        return True
