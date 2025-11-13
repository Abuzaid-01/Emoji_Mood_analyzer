# data_loader.py
# Part 1 of Mini ML Workflow Simulator
# Role: Handles data ingestion (like reading from a database or file)

class DataLoader:
    """
    DataLoader class simulates the data ingestion phase of an ML pipeline.
    In real ML systems, this would read from files, databases, or APIs.
    """
    
    def __init__(self):
        """
        Initialize the data loader with a sample dataset.
        In real scenarios, this could read from CSV, JSON, or databases.
        """
        # Sample dataset: could represent prices, temperatures, scores, etc.
        self.data = [12, 15, 18, 20, 22]
        self.dataset_name = "Sample Numeric Dataset"
    
    def get_data(self):
        """
        Return the loaded data.
        
        Returns:
            list: The dataset as a list of numbers
        """
        return self.data
    
    def get_stats(self):
        """
        Get basic statistics about the dataset.
        
        Returns:
            dict: Dictionary containing dataset statistics
        """
        return {
            'size': len(self.data),
            'min': min(self.data),
            'max': max(self.data),
            'sum': sum(self.data)
        }
    
    def display_info(self):
        """Display information about the loaded data."""
        print(f"Dataset: {self.dataset_name}")
        print(f"Data: {self.data}")
        stats = self.get_stats()
        print(f"Size: {stats['size']} samples")
        print(f"Range: {stats['min']} to {stats['max']}")
