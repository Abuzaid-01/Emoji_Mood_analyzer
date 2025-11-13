# TASK 4 — Word Frequency Finder
# Goal: Take a paragraph and show which words appear most often

import string

def word_frequency_finder():
    # Get input from user
    text = input("Enter a paragraph: ")
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    for punct in string.punctuation:
        text = text.replace(punct, "")
    
    # Split into words
    words = text.split()
    
    # Count each word using a dictionary
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Sort by count in descending order
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    # Display results
    print("\n" + "="*50)
    print("WORD FREQUENCY ANALYSIS")
    print("="*50)
    print(f"\nTotal words: {len(words)}")
    print(f"Unique words: {len(word_count)}")
    
    # Show top 3 most frequent words
    print("\n--- Top 3 Most Frequent Words ---")
    top_3 = sorted_words[:3]
    
    for i, (word, count) in enumerate(top_3, 1):
        print(f"{i}. '{word}' - appears {count} time(s)")
    
    # Optional: Show all word frequencies
    print("\n--- All Word Frequencies ---")
    for word, count in sorted_words:
        print(f"'{word}': {count}")

if __name__ == "__main__":
    word_frequency_finder()
