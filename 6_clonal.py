import numpy as np

# ------------------------------
# 🎯 Step 1: Initialization
# ------------------------------
population_size = 20
dimension = 2
lower_bound = -5.12
upper_bound = 5.12
num_generations = 30
clone_factor = 5
mutation_rate = 0.2

# ✅ Rastrigin Function (Minimization, but returns positive value)
def fitness_function(x):
    return 10 * len(x) + sum([xi**2 - 10 * np.cos(2 * np.pi * xi) for xi in x])  # Always ≥ 0

# Generate initial population
def initialize_population():
    return np.random.uniform(lower_bound, upper_bound, (population_size, dimension))

population = initialize_population()

# ------------------------------
# 🔍 Step 2: Clonal Selection
# ------------------------------
def evaluate_fitness(population):
    return np.array([fitness_function(ind) for ind in population])

# ------------------------------
# 🧬 Step 3: Cloning
# ------------------------------
def clone_population(population, fitnesses):
    clones = []
    # Lower fitness = better, so rank in ascending order
    fit_ranks = np.argsort(fitnesses)  # ascending
    for rank in fit_ranks:
        num_clones = clone_factor
        for _ in range(num_clones):
            clones.append(np.copy(population[rank]))
    return np.array(clones)

# ------------------------------
# 🔁 Step 4: Mutation
# ------------------------------
def mutate(clones):
    for i in range(len(clones)):
        if np.random.rand() < mutation_rate:
            clones[i] += np.random.normal(0, 0.5, size=clones[i].shape)
            clones[i] = np.clip(clones[i], lower_bound, upper_bound)
    return clones

# ------------------------------
# ♻️ Step 5: Replacement
# ------------------------------
def select_top(clones, fitnesses, size):
    sorted_indices = np.argsort(fitnesses)  # ascending (min fitness = best)
    unique = []
    seen = set()
    for idx in sorted_indices:
        candidate = tuple(clones[idx])
        if candidate not in seen:
            unique.append(clones[idx])
            seen.add(candidate)
        if len(unique) == size:
            break
    return np.array(unique)

# ------------------------------
# 🔁 Step 6: Repeat Loop
# ------------------------------
for gen in range(num_generations):
    fitnesses = evaluate_fitness(population)
    clones = clone_population(population, fitnesses)
    clones = mutate(clones)
    clone_fitnesses = evaluate_fitness(clones)
    population = select_top(clones, clone_fitnesses, population_size)

    best_fitness = min(clone_fitnesses)  # lowest value is best
    print(f"Generation {gen+1}: Best Fitness = {best_fitness:.4f}")

# ------------------------------
# 🏁 Step 7 & 8: Final Solution
# ------------------------------
final_fitnesses = evaluate_fitness(population)
best_idx = np.argmin(final_fitnesses)  # get best solution
best_solution = population[best_idx]

print("\n✅ Best Solution:", best_solution)
print("✅ Best Fitness (minimized Rastrigin):", final_fitnesses[best_idx])
