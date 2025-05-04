from collections import defaultdict
import re

# ---------------- MAP PHASE ----------------
def mapper(lines):
    mapped = []
    for line in lines:
        words = re.findall(r'\b\w+\b', line.lower())  # extract words
        for word in words:
            mapped.append((word, 1))  # Emit (word, 1)
    return mapped

# ---------------- SHUFFLE + SORT PHASE ----------------
def shuffle_sort(mapped_data):
    shuffled = defaultdict(list)
    for word, count in mapped_data:
        shuffled[word].append(count)  # Group all 1's by word
    return shuffled

# ---------------- REDUCE PHASE ----------------
def reducer(shuffled_data):
    reduced = {}
    for word, counts in shuffled_data.items():
        reduced[word] = sum(counts)  # Sum all counts
    return reduced

# ---------------- DRIVER FUNCTION ----------------
def run_mapreduce(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    mapped = mapper(lines)                 # Step 1: Map
    shuffled = shuffle_sort(mapped)        # Step 2: Shuffle + Sort
    reduced = reducer(shuffled)            # Step 3: Reduce

    print("Word Count:")
    for word, count in sorted(reduced.items()):
        print(f"'{word}': {count}")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    run_mapreduce("sample.txt")  # Ensure sample.txt exists
