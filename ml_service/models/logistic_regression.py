from .base_model import BaseModel
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class LogisticRegressionModel(BaseModel):

    def __init__(self):
        self.model = LogisticRegression()

    def train(self, x, y):
        self.model.fit(x, y)
   

    def predict(self, X):
        result = self.model.predict(X)
        return result

    def evaluate(self, x_test, y_test):
        predictions = self.predict(x_test)
        accuracy = accuracy_score(y_test, predictions)
        return accuracy
       