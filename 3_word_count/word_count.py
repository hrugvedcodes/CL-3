import multiprocessing
from collections import defaultdict
import re

# ----------------------- Mapper Function -----------------------
def mapper(chunk):
    freq = defaultdict(int)
    for line in chunk:
        words = re.findall(r'\b\w+\b', line.lower())  # extract words
        for word in words:
            freq[word] += 1
    return freq

# ----------------------- Reducer Function -----------------------
def reducer(mapped_data):
    result = defaultdict(int)
    for partial_dict in mapped_data:
        for word, count in partial_dict.items():
            result[word] += count
    return result

# ---------------------- MapReduce Driver -----------------------
def word_count_mapreduce(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    num_workers = multiprocessing.cpu_count()
    chunk_size = max(1, len(lines) // num_workers)
    chunks = [lines[i:i + chunk_size] for i in range(0, len(lines), chunk_size)]

    with multiprocessing.Pool(processes=num_workers) as pool:
        mapped = pool.map(mapper, chunks)  # map step

    reduced = reducer(mapped)  # reduce step

    print("Word Count:")
    for word, count in sorted(reduced.items()):
        print(f"{word}: {count}")

# ---------------------- Entry Point -----------------------
if __name__ == "__main__":
    word_count_mapreduce("sample.txt")  # Ensure this file exists
