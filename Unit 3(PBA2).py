import re
from collections import Counter


def find_duplicate_words(sentence: str):
  # Extract all whole words using regex, converting to lowercase for uniformity
  words = re.findall(r"\b\w+\b", sentence.lower())

  # Count word frequencies
  word_counts = Counter(words)

  # Filter words that appear more than once
  duplicates = [word for word, count in word_counts.items() if count > 1]
  return duplicates


# Example usage
text = "The quick brown fox jumps over the lazy dog, but the dog was not lazy."
result = find_duplicate_words(text)
print("Words occurring more than once:", result)
