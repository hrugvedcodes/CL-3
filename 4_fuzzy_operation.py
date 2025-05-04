# Fuzzy Union
def fuzzy_union(A, B):
    result = {}
    keys = []

    for key in A:
        if key not in keys:
            keys.append(key)                        
                                                    
    for key in B:
        if key not in keys:
            keys.append(key)

    for key in keys:
        valA = A[key] if key in A else 0
        valB = B[key] if key in B else 0
        result[key] = valA if valA > valB else valB
    return result

# Fuzzy Intersection
def fuzzy_intersection(A, B):
    result = {}
    for key in A:
        if key in B:
            result[key] = A[key] if A[key] < B[key] else B[key]
    return result

# Fuzzy Difference
def fuzzy_difference(A, B):
    result = {}
    for key in A:
        valB = B[key] if key in B else 0
        diff = A[key] - valB
        result[key] = diff if diff > 0 else 0
    return result

# Fuzzy Complement
def fuzzy_complement(A):
    result = {}
    for key in A:
        result[key] = round(1 - A[key], 2)
    return result


# Cartesian Product
def cartesian_product(A, B):
    result = {}
    for a in A:
        for b in B:
            result[(a, b)] = A[a] if A[a] < B[b] else B[b]
    return result

# Max-Min Composition
def max_min_composition(R1, R2):
    result = {}
    # Get all 'a' from R1
    a_values = []
    for (i, j) in R1:
        if i not in a_values:
            a_values.append(i)

    # Get all 'c' from R2
    c_values = []
    for (i, j) in R2:
        if j not in c_values:
            c_values.append(j)

    # Get all 'b' from R1
    b_values = []
    for (i, j) in R1:
        if j not in b_values:
            b_values.append(j)

    for a in a_values:
        for c in c_values:
            min_vals = []
            for b in b_values:
                val1 = R1[(a, b)] if (a, b) in R1 else 0
                val2 = R2[(b, c)] if (b, c) in R2 else 0
                min_val = val1 if val1 < val2 else val2
                min_vals.append(min_val)

            # Find max of min_vals
            max_val = min_vals[0]
            for v in min_vals:
                if v > max_val:
                    max_val = v
            result[(a, c)] = max_val
    return result

# Example Fuzzy Sets
A = {"x": 0.3, "y": 0.7}
B = {"x": 0.6, "z": 0.8}

print("Union:", fuzzy_union(A, B))
print("Intersection:", fuzzy_intersection(A, B))
print("Difference A - B:", fuzzy_difference(A, B))
print("Complement of A:", fuzzy_complement(A))

R1 = cartesian_product(A, B)
R2 = cartesian_product(B, A)
print("Cartesian Product (R1):", R1)
print("Max-Min Composition of R1 and R2:", max_min_composition(R1, R2))
