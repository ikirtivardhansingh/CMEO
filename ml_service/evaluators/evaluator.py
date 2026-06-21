from sklearn.metrics import accuracy_score
class Evaluator:
    def evaluate(self, y_true, y_pred):
        accuracy = accuracy_score(y_true, y_pred)
        return accuracy
    