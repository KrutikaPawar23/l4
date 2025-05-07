import numpy as np
import random

# Rastrigin Function (Optimization Objective)
def rastrigin(x):
    A = 10
    return A * len(x) + sum(x_i**2 - A * np.cos(2 * np.pi * x_i) for x_i in x)

# Clonal Selection Algorithm
def clonal_selection_algorithm(pop_size, generations, mutation_rate, elite_size):
    # Step 1: Initialize population with random values between -5.12 and 5.12
    population = np.random.uniform(-5.12, 5.12, (pop_size, 2))  # 2D Rastrigin Problem
    
    # Step 2: Start evolution for 'generations' number of generations
    for gen in range(generations):
        # Step 3: Calculate the fitness for each individual in the population
        fitness = np.array([rastrigin(ind) for ind in population])

        # Step 4: Select the best (elite) individuals based on their fitness
        elite_indices = np.argsort(fitness)[:elite_size]  # Get the indices of the elite individuals
        elite_individuals = population[elite_indices]

        # Step 5: Clone the best individuals
        clones = elite_individuals.copy()

        # Step 6: Mutate the clones slightly (explore new solutions)
        for i in range(len(clones)):
            if random.random() < mutation_rate:
                clones[i] += np.random.uniform(-0.1, 0.1, 2)  # Small random change
                clones[i] = np.clip(clones[i], -5.12, 5.12)  # Ensure values are within the bounds

        # Step 7: Replace the worst individuals with the best clones
        worst_indices = np.argsort(fitness)[-elite_size:]  # Get indices of the worst individuals
        population[worst_indices] = clones

        # Step 8: Output the best solution of the current generation
        best_solution = population[np.argmin(fitness)]  # Best individual has minimum fitness
        print(f"Generation {gen+1}, Best Solution: {best_solution}, Fitness: {rastrigin(best_solution)}")

# Parameters for the algorithm
population_size = 20  # Number of individuals
generations = 50  # Number of generations to evolve
mutation_rate = 0.1  # Chance of mutation in each clone
elite_size = 4  # Number of elite individuals to keep

# Run Clonal Selection Algorithm
clonal_selection_algorithm(population_size, generations, mutation_rate, elite_size)

#Krutika Pawar Rollno 30
#OUTPUT
#

# Generation 1, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 2, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 3, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 4, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 5, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 6, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 7, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 8, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 9, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 10, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 11, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 12, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 13, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 14, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 15, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 16, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 17, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 18, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 19, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 20, Best Solution: [ 0.04470995 -1.92992324], Fitness: 5.072381409018055
# Generation 21, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 22, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 23, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 24, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 25, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 26, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 27, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 28, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 29, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 30, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 31, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 32, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 33, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 34, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 35, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 36, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 37, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 38, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 39, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 40, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 41, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 42, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 43, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 44, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 45, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 46, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 47, Best Solution: [-0.05108348 -1.98134782], Fitness: 4.5076355474875776
# Generation 48, Best Solution: [ 0.02719306 -1.94808866], Fitness: 4.468628700356602
# Generation 49, Best Solution: [ 0.02719306 -1.94808866], Fitness: 4.468628700356602
# Generation 50, Best Solution: [ 8.6641767e-04 -1.9668934e+00], Fitness: 4.084390568701238