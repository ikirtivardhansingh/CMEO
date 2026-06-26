from .base_model import BaseModel
from sklearn.ensemble import RandomForestClassifier

class RandomForestClassificationModel(BaseModel):

    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, x, y):
        self.model.fit(x, y)

    def predict(self, X):
        result = self.model.predict(X)
        return result
    