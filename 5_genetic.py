import numpy as np
import random

# STEP 1: Initial Population
def initialize_population(pop_size, dimension, lower_bound, upper_bound):
    return np.random.uniform(lower_bound, upper_bound, (pop_size, dimension))

# STEP 2: Fitness Function (e.g., minimize the Rastrigin function)
def fitness_function(individual):
    return 10 * len(individual) + sum([x**2 - 10 * np.cos(2 * np.pi * x) for x in individual])

# STEP 3: Selection (Tournament Selection)
def tournament_selection(population, fitnesses, k=3):
    selected = []
    for _ in range(len(population)):
        competitors = random.sample(list(zip(population, fitnesses)), k)
        winner = min(competitors, key=lambda x: x[1])  # Minimizing fitness
        selected.append(winner[0])
    return np.array(selected)

# STEP 4: Crossover (Single-Point Crossover)
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:point], parent2[point:]))
    child2 = np.concatenate((parent2[:point], parent1[point:]))
    return child1, child2

# STEP 5: Mutation (Gaussian Mutation)
def mutate(individual, mutation_rate, lower_bound, upper_bound):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] += np.random.normal(0, 0.1)
            individual[i] = np.clip(individual[i], lower_bound, upper_bound)
    return individual

# STEP 6-7: Main Genetic Algorithm Loop
def genetic_algorithm():
    pop_size = 20
    generations = 50
    dimension = 2
    lower_bound = -5.12
    upper_bound = 5.12
    mutation_rate = 0.1

    # Initialize population
    population = initialize_population(pop_size, dimension, lower_bound, upper_bound)

    for gen in range(generations):
        # Evaluate fitness of each individual
        fitnesses = [fitness_function(ind) for ind in population]

        # Selection: Choose the best individuals as parents
        selected_parents = tournament_selection(population, fitnesses)

        # Crossover: Generate offspring
        next_population = []
        for i in range(0, pop_size, 2):
            parent1 = selected_parents[i]
            parent2 = selected_parents[(i + 1) % pop_size]
            child1, child2 = crossover(parent1, parent2)
            next_population.extend([child1, child2])

        # Mutation: Mutate offspring
        population = np.array([mutate(ind, mutation_rate, lower_bound, upper_bound) for ind in next_population])

        # Evaluate fitness again
        best_fitness = min([fitness_function(ind) for ind in population])
        print(f"Generation {gen+1}: Best Fitness = {best_fitness:.4f}")

    # Final best individual
    final_fitnesses = [fitness_function(ind) for ind in population]
    best_individual = population[np.argmin(final_fitnesses)]
    print("\nBest Solution Found:", best_individual)
    print("Best Fitness:", fitness_function(best_individual))

# Run the algorithm
genetic_algorithm()
