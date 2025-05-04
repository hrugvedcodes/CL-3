import random
import numpy as np
from deap import base, creator, tools

# ------------------------------
# Step 1: Initialization
# ------------------------------
IND_SIZE = 2  # Number of parameters (dimensions)
POP_SIZE = 20  # Population size
N_GEN = 30     # Number of generations

# ------------------------------
# Step 2: Define Fitness Function
# ------------------------------
def rastrigin(ind):
    A = 10
    return -(A * len(ind) + sum([(x**2 - A * np.cos(2 * np.pi * x)) for x in ind])),  # maximize → so negative

# ------------------------------
# Step 3: Genetic Operators Setup
# ------------------------------
creator.create("FitnessMax", base.Fitness, weights=(1.0,))  # Maximization
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -5.12, 5.12)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=IND_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", rastrigin)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# ------------------------------
# Step 4: Evaluate Population
# ------------------------------
population = toolbox.population(n=POP_SIZE)

# ------------------------------
# Step 5–9: Evolution Loop
# ------------------------------
for gen in range(N_GEN):
    # Step 4: Evaluate
    for ind in population:
        ind.fitness.values = toolbox.evaluate(ind)

    # Step 5: Selection
    offspring = toolbox.select(population, len(population))
    offspring = list(map(toolbox.clone, offspring))

    # Step 6: Crossover
    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < 0.7:
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

    # Step 7: Mutation
    for mutant in offspring:
        if random.random() < 0.2:
            toolbox.mutate(mutant)
            del mutant.fitness.values

    # Step 8: Evaluate Offspring
    for ind in offspring:
        if not ind.fitness.valid:
            ind.fitness.values = toolbox.evaluate(ind)

    # Step 9: Replacement
    population[:] = offspring

    # Print best of generation
    top = tools.selBest(population, 1)[0]
    print(f"Generation {gen+1}: Best Fitness = {top.fitness.values[0]:.4f}")

# ------------------------------
# Step 10: Final Solution
# ------------------------------
best_solution = tools.selBest(population, 1)[0]
print("\nBest Solution Found:", best_solution)
print("Best Fitness:", best_solution.fitness.values[0])
