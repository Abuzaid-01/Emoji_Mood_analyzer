# TASK 6 - Smart Sensor Classifier
# Goal: Simulate how AI models classify inputs using OOP

import random

class Sensor:
    """
    A sensor class that classifies numeric values into Low, Medium, or High categories.
    Simulates how AI models use decision boundaries for classification.
    """
    
    def __init__(self, name, low_threshold, high_threshold):
        """
        Initialize a sensor with name and threshold values.
        
        Args:
            name: Name of the sensor (e.g., "Temperature", "Humidity")
            low_threshold: Upper bound for "Low" category
            high_threshold: Lower bound for "High" category
        """
        self.name = name
        self.low_threshold = low_threshold
        self.high_threshold = high_threshold
    
    def classify(self, value):
        """
        Classify a sensor reading into Low, Medium, or High.
        
        Args:
            value: The numeric reading to classify
        """
        if value < self.low_threshold:
            category = "🔵 LOW"
            emoji = "❄️"
        elif value >= self.high_threshold:
            category = "🔴 HIGH"
            emoji = "🔥"
        else:
            category = "🟡 MEDIUM"
            emoji = "✅"
        
        print(f"{emoji} {self.name}: {value}°C → {category}")
        return category
    
    def get_info(self):
        """Display sensor configuration information."""
        print(f"\n--- {self.name} Sensor ---")
        print(f"Low threshold: < {self.low_threshold}")
        print(f"Medium range: {self.low_threshold} - {self.high_threshold}")
        print(f"High threshold: >= {self.high_threshold}")


def main():
    print("="*60)
    print("SMART SENSOR CLASSIFIER SYSTEM")
    print("="*60)
    
    # Create different sensors with different thresholds
    temp_sensor = Sensor("Temperature", 20, 30)
    humidity_sensor = Sensor("Humidity", 40, 60)
    pressure_sensor = Sensor("Pressure", 990, 1010)
    
    # Display sensor configurations
    temp_sensor.get_info()
    humidity_sensor.get_info()
    pressure_sensor.get_info()
    
    # Test with random values
    print("\n" + "="*60)
    print("RUNNING SENSOR TESTS (3 readings per sensor)")
    print("="*60)
    
    print("\n--- Temperature Readings ---")
    for i in range(3):
        temp_value = random.randint(10, 40)
        temp_sensor.classify(temp_value)
    
    print("\n--- Humidity Readings ---")
    for i in range(3):
        humidity_value = random.randint(20, 80)
        humidity_sensor.classify(humidity_value)
    
    print("\n--- Pressure Readings ---")
    for i in range(3):
        pressure_value = random.randint(980, 1020)
        pressure_sensor.classify(pressure_value)
    
    # Interactive mode
    print("\n" + "="*60)
    print("INTERACTIVE MODE")
    print("="*60)
    
    choice = input("\nWould you like to test a custom value? (yes/no): ").lower()
    
    if choice in ['yes', 'y']:
        print("\nAvailable sensors:")
        print("1. Temperature (Low: <20, High: >=30)")
        print("2. Humidity (Low: <40, High: >=60)")
        print("3. Pressure (Low: <990, High: >=1010)")
        
        sensor_choice = input("\nChoose sensor (1/2/3): ")
        try:
            value = float(input("Enter value to classify: "))
            
            if sensor_choice == '1':
                temp_sensor.classify(value)
            elif sensor_choice == '2':
                humidity_sensor.classify(value)
            elif sensor_choice == '3':
                pressure_sensor.classify(value)
            else:
                print("Invalid sensor choice!")
        except ValueError:
            print("Invalid value entered!")
    
    print("\n" + "="*60)
    print("Classification Complete!")
    print("="*60)


if __name__ == "__main__":
    main()
