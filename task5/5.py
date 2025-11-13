# TASK 5 — Trend Tracker
# Goal: Detect if trend is rising, falling, or stable and predict next value

def trend_tracker():
    # Predefined list of values (e.g., daily temperatures or stock prices)
    values = [30, 31, 33, 34, 35]
    
    print("="*50)
    print("TREND TRACKER")
    print("="*50)
    print(f"\nOriginal values: {values}")
    
    # Find consecutive differences
    differences = []
    for i in range(1, len(values)):
        diff = values[i] - values[i-1]
        differences.append(diff)
    
    print(f"Consecutive differences: {differences}")
    
    # Calculate average difference
    avg_diff = sum(differences) / len(differences)
    print(f"Average difference: {avg_diff:.2f}")
    
    # Detect trend
    if avg_diff > 0.5:
        trend = "RISING ↑"
    elif avg_diff < -0.5:
        trend = "FALLING ↓"
    else:
        trend = "STABLE →"
    
    print(f"\nTrend: {trend}")
    
    # Predict next value
    next_value = values[-1] + avg_diff
    print(f"Predicted next value: {next_value:.2f}")
    
    # Additional insights
    print("\n--- Additional Insights ---")
    print(f"Current value: {values[-1]}")
    print(f"Minimum value: {min(values)}")
    print(f"Maximum value: {max(values)}")
    print(f"Average value: {sum(values) / len(values):.2f}")

# Extended version with user input
def trend_tracker_custom():
    print("="*50)
    print("TREND TRACKER - CUSTOM INPUT")
    print("="*50)
    
    # Get custom values from user
    user_input = input("\nEnter values separated by spaces (e.g., 30 31 33 34 35): ")
    values = [float(x) for x in user_input.split()]
    
    if len(values) < 2:
        print("Error: Need at least 2 values to detect a trend!")
        return
    
    print(f"\nYour values: {values}")
    
    # Find consecutive differences
    differences = []
    for i in range(1, len(values)):
        diff = values[i] - values[i-1]
        differences.append(diff)
    
    print(f"Consecutive differences: {differences}")
    
    # Calculate average difference
    avg_diff = sum(differences) / len(differences)
    print(f"Average difference: {avg_diff:.2f}")
    
    # Detect trend
    if avg_diff > 0.5:
        trend = "RISING ↑"
        description = "The values are increasing over time."
    elif avg_diff < -0.5:
        trend = "FALLING ↓"
        description = "The values are decreasing over time."
    else:
        trend = "STABLE →"
        description = "The values are relatively stable."
    
    print(f"\nTrend: {trend}")
    print(f"Description: {description}")
    
    # Predict next value
    next_value = values[-1] + avg_diff
    print(f"\nPredicted next value: {next_value:.2f}")
    
    # Confidence indicator
    variance = sum((d - avg_diff) ** 2 for d in differences) / len(differences)
    if variance < 0.5:
        confidence = "HIGH"
    elif variance < 2:
        confidence = "MEDIUM"
    else:
        confidence = "LOW"
    
    print(f"Prediction confidence: {confidence}")

if __name__ == "__main__":
    # Run basic version
    trend_tracker()
    
    # Ask if user wants to try custom input
    print("\n" + "="*50)
    choice = input("\nWould you like to try with custom values? (yes/no): ").lower()
    
    if choice in ['yes', 'y']:
        print()
        trend_tracker_custom()
