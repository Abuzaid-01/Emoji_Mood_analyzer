# main.py
# Part 3 of Mini ML Workflow Simulator
# Role: Orchestrates the entire ML pipeline - loads data, trains model, makes predictions

from data_loader import DataLoader
from simple_model import SimpleModel

def main():
    """
    Main function that runs the complete ML workflow.
    This simulates a real machine learning pipeline:
    1. Data Loading
    2. Model Training
    3. Prediction/Inference
    """
    
    print("="*70)
    print("MINI ML WORKFLOW SIMULATOR")
    print("="*70)
    
    # STEP 1: DATA LOADING
    print("\n📁 STEP 1: LOADING DATA")
    print("-" * 70)
    
    loader = DataLoader()
    data = loader.get_data()
    loader.display_info()
    
    # STEP 2: MODEL TRAINING
    print("\n" + "="*70)
    print("🧠 STEP 2: TRAINING MODEL")
    print("-" * 70)
    
    model = SimpleModel()
    model.train(data)
    model.get_model_info()
    
    # STEP 3: MAKING PREDICTIONS
    print("\n" + "="*70)
    print("🔮 STEP 3: MAKING PREDICTIONS")
    print("-" * 70)
    
    # Test on various values
    test_values = [10, 17, 20, 25]
    
    print(f"\nTesting {len(test_values)} values:")
    print(f"Model average (decision boundary): {model.avg:.2f}")
    print("\nResults:")
    
    for val in test_values:
        result = model.predict(val)
        print(f"  Value {val:2d} → {result}")
    
    # STEP 4: ADVANCED PREDICTIONS WITH CONFIDENCE
    print("\n" + "="*70)
    print("📊 STEP 4: PREDICTIONS WITH CONFIDENCE")
    print("-" * 70)
    
    advanced_test_values = [5, 15, 18, 30]
    
    print(f"\nAdvanced testing on {len(advanced_test_values)} values:\n")
    
    for val in advanced_test_values:
        prediction, confidence = model.predict_with_confidence(val)
        print(f"  Value {val:2d} → {prediction:20s} | Confidence: {confidence:.1f}%")
    
    # STEP 5: INTERACTIVE PREDICTION
    print("\n" + "="*70)
    print("🎮 INTERACTIVE MODE")
    print("-" * 70)
    
    choice = input("\nWould you like to test your own value? (yes/no): ").lower()
    
    if choice in ['yes', 'y']:
        try:
            custom_value = float(input("\nEnter a value to classify: "))
            prediction, confidence = model.predict_with_confidence(custom_value)
            
            print("\n" + "-" * 70)
            print(f"Your value: {custom_value}")
            print(f"Model average: {model.avg:.2f}")
            print(f"Prediction: {prediction}")
            print(f"Confidence: {confidence:.1f}%")
            print("-" * 70)
            
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")
    
    # SUMMARY
    print("\n" + "="*70)
    print("✅ ML WORKFLOW COMPLETED SUCCESSFULLY!")
    print("="*70)
    print("\n📋 Summary:")
    print(f"   • Data samples loaded: {len(data)}")
    print(f"   • Model trained on: {data}")
    print(f"   • Learned parameter (average): {model.avg:.2f}")
    print(f"   • Total predictions made: {len(test_values) + len(advanced_test_values)}")
    
    print("\n💡 This workflow mirrors real ML systems:")
    print("   1. data_loader.py → Data ingestion layer")
    print("   2. simple_model.py → Model/algorithm layer")
    print("   3. main.py → Pipeline orchestration layer")
    print("="*70)


if __name__ == "__main__":
    main()
