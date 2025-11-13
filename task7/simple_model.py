# simple_model.py
# Part 2 of Mini ML Workflow Simulator
# Role: Represents the ML model with training and prediction capabilities

class SimpleModel:
    """
    SimpleModel class simulates a basic machine learning model.
    It learns the average from training data and makes predictions based on it.
    In real ML, this would be a neural network, decision tree, etc.
    """
    
    def __init__(self):
        """
        Initialize the model.
        avg: will store the learned average after training
        is_trained: tracks whether the model has been trained
        """
        self.avg = None
        self.is_trained = False
        self.training_data_size = 0
    
    def train(self, data):
        """
        Train the model on the provided data.
        This is a simple "learning" process - computing the average.
        
        Args:
            data: List of numbers to train on
        """
        if not data:
            print("❌ Error: Cannot train on empty data!")
            return
        
        # Compute the average (this is our "learning" step)
        self.avg = sum(data) / len(data)
        self.is_trained = True
        self.training_data_size = len(data)
        
        print(f"✅ Model trained successfully!")
        print(f"   Training samples: {self.training_data_size}")
        print(f"   Learned average: {self.avg:.2f}")
    
    def predict(self, x):
        """
        Make a prediction for a given value.
        Compares the value to the learned average.
        
        Args:
            x: The value to predict/classify
            
        Returns:
            str: Classification result ("Above Average" or "Below Average")
        """
        if not self.is_trained:
            return "❌ Error: Model not trained yet!"
        
        if x > self.avg:
            return "📈 Above Average"
        elif x < self.avg:
            return "📉 Below Average"
        else:
            return "🎯 Exactly Average"
    
    def predict_with_confidence(self, x):
        """
        Make a prediction with confidence score.
        
        Args:
            x: The value to predict/classify
            
        Returns:
            tuple: (prediction, confidence_percentage)
        """
        if not self.is_trained:
            return ("Error: Model not trained", 0)
        
        prediction = self.predict(x)
        
        # Calculate confidence based on distance from average
        distance = abs(x - self.avg)
        max_distance = self.avg  # Normalize by average value
        confidence = min(100, (distance / max_distance) * 100) if max_distance != 0 else 50
        
        return prediction, confidence
    
    def get_model_info(self):
        """Display model information."""
        if self.is_trained:
            print(f"\n--- Model Information ---")
            print(f"Status: ✅ Trained")
            print(f"Learned average: {self.avg:.2f}")
            print(f"Training samples: {self.training_data_size}")
        else:
            print(f"\n--- Model Information ---")
            print(f"Status: ❌ Not trained")
