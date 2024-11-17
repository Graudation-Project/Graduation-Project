class MlDevelopmentLifeCycle:
    def __init__(self):
        self.iterations = 0
        self.iteration_history = []

    def execute_cycle(self):
        
        data = self.preprocess_data()

        model = self.model_selection()

        metrics = self.evaluate_model(model)

    

    def preprocess_data(self):
        pass

    def model_selection(self):
        pass

    def evaluate_model(self,model):
        pass

    