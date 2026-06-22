class ModelRegistry:

    def __init(self):
        self.model = None

    def save_model(self, model):
        self.model = model

    def get_model(self):
        return self.model
registry = ModelRegistry()