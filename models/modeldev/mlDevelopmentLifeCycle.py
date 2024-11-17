class mlDevelopmentLifeCycle:
    def __init__(self):
        self.current_iteration = 0
        self.performance_history = []

    def execute_iteration(self):

        # Data Preprocessing
        data = self.preprocess_data()

        # Select Best Model
        model = self.model_selection()

        # Getting Model Metrics
        metrics = self.evaluate_model(model)

    
    def preprocess_data(self):
        pass

    def model_selection(self):
        pass

    def evaluate_model(self,model):
        pass