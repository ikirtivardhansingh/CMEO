import pandas as pd
import json
from ml_service.services.validator import Validator
from ml_service.preprocessors.preprocessor import Preprocessor
from ml_service.models.logistic_regression import LogisticRegressionModel
from ml_service.evaluators.evaluator import Evaluator
from ml_service.model_registry import registry

class DatasetLoader:

    def load(self, file_path):
        return pd.read_csv(file_path)
with open("configs/churn_config.json", "r") as file:
    config = json.load(file)
    
loader = DatasetLoader()

df = loader.load("datasets/tcc.csv")

print(df.head())
print(df.columns)

validator = Validator()
validator.validate_not_empty(df)
validator.validate_target_column(
    df,
    config["target_column"]
)
validator.validate_required_columns(
    df,
    config[
        "validation_req_columns"
    ]
)

print("All validations passed")


preprocessor = Preprocessor()

processed_data = preprocessor.process(
    df,
    selected_features=config["selected_features"],
    target_column=config["target_column"],
    drop_columns=config["drop_columns"],
    binary_columns=config[
        "binary_columns"
    ],
    categorical_columns=config[
        "categorical_columns"
    ],
    numerical_columns=config["numerical_columns"]
)
print(processed_data["X_train"].columns)
model = LogisticRegressionModel()

model.train(processed_data["X_train"],
            processed_data["y_train"]
)

import joblib
joblib.dump(model, "RegressionModel.pkl")

registry.save_model(model)

evaluator = Evaluator()
predictions = model.predict(
    processed_data["X_test"]
)

evaluation_result = evaluator.evaluate(
    processed_data["y_test"],
    predictions
)
print("Accuracy:", evaluation_result)
