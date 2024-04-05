import re
from collections import Counter

def count_words(filename):
    # Read the file and convert all text to lowercase
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    # Use regex to find all words (including numbers, apostrophes, and hyphens)
    words = re.findall(r"\b[a-zA-Z0-9'-]+\b", text)

    # Count the frequency of each word
    word_counts = Counter(words)

    # Print total word count
    total_words = len(words)
    print(f"Total words: {total_words}\n")

    # Print the top 20 most frequent words and their counts
    print("Top 20 most frequent words:")
    for word, count in word_counts.most_common(20):
        print(f"{word}: {count}")

# Example usage
count_words('shakespeare.txt')
