from collections import defaultdict

# MAP PHASE
def mapper(lines):
    mapped = []
    for line in lines:
        for char in line:
            if not char.isspace():            
                mapped.append((char.lower(), 1))  # Emit (char, 1)
    return mapped

# SHUFFLE + SORT PHASE
def shuffle_sort(mapped_data):
    shuffled = defaultdict(list)  
    for char, count in mapped_data: 
        shuffled[char].append(count)  # Group all 1's by character
    return shuffled

# REDUCE PHASE
def reducer(shuffled_data):
    reduced = {}
    for char, counts in shuffled_data.items(): 
        reduced[char] = sum(counts)  # Sum all 1's for each character
    return reduced

# DRIVER FUNCTION
def run_mapreduce(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    mapped = mapper(lines)                     # Step 1: Map
    shuffled = shuffle_sort(mapped)            # Step 2: Shuffle + Sort
    reduced = reducer(shuffled)                # Step 3: Reduce

    print("Character Count:")
    for char, count in sorted(reduced.items()):
        print(f"'{char}': {count}")

# MAIN
if __name__ == "__main__":
    run_mapreduce("sample.txt")  # Make sure sample.txt exists
