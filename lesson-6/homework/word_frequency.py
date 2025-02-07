import os
import string
import json
from collections import Counter

STOP_WORDS = {"the", "and", "is", "in", "to", "of", "a", "that", "it", "on", "for", "with"}

def count_word_frequency(filename, top_n=5):
    """Counts word frequencies in the specified file and returns the results."""
    if not os.path.exists(filename):
        print("File not found.")
        return
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        # Normalize text by removing punctuation and converting to lowercase
        translator = str.maketrans("", "", string.punctuation)
        words = text.lower().translate(translator).split()

        # Remove stop words
        words = [word for word in words if word not in STOP_WORDS]

        # Count word occurrences
        word_counts = Counter(words)

        # Save report to a file
        report_data = {
            "total_words": len(words),
            "unique_words": len(word_counts),
            "top_words": word_counts.most_common(top_n)
        }
        report_file = "word_count_report.json"
        with open(report_file, "w", encoding="utf-8") as report:
            json.dump(report_data, report, indent=4)

        print("\nWord Frequency Analysis:")
        print(f"Total words: {len(words)}")
        print(f"Unique words: {len(word_counts)}")
        print(f"Top {top_n} most common words:")
        for word, count in word_counts.most_common(top_n):
            print(f"{word} - {count} times")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    filename = input("Enter the file name to analyze: ").strip()
    try:
        top_n = int(input("Enter the number of top common words to display (default 5): ").strip() or 5)
    except ValueError:
        top_n = 5
    count_word_frequency(filename, top_n)
