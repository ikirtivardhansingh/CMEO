from .base_model import BaseModel
from sklearn.linear_model import LogisticRegression


class LogisticRegressionModel(BaseModel):

    def __init__(self):
        self.model = LogisticRegression()

    def train(self, x, y):
        self.model.fit(x, y)
   

    def predict(self, X):
        result = self.model.predict(X)
        return result


       