from .base_model import BaseModel
from sklearn.tree import DecisionTreeClassifier

class DecisionTreeModel(BaseModel):
    def __init__(self):
        self.model = DecisionTreeClassifier()

    def train(self, x, y):
        self.model.fit(x, y)

    def predict(self, X):
        result = self.modelpredict(X)
        return result