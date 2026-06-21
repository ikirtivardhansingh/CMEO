class Validator:
    
    def validate_target_column(self, df, target_column):
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
    def validate_required_columns(self, df, required_columns):
        
        for column in required_columns:
            if column not in df.columns:
                raise ValueError(
                    f"Required column '{columns}' not found in the dataset"
                )
            
            return True
