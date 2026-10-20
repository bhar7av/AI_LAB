"""Lab 8: A simple genetic algorithm that evolves a bit string of all ones."""

import random


CHROMOSOME_LENGTH = 10
POPULATION_SIZE = 20
GENERATIONS = 60
MUTATION_RATE = 0.02


def make_chromosome():
    return [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]


def fitness(chromosome):
    """The more 1s, the higher the fitness."""
    return sum(chromosome)


def select_parent(population):
    """Tournament selection: the fittest of three random candidates wins."""
    candidates = random.sample(population, 3)
    return max(candidates, key=fitness)


def crossover(parent_a, parent_b):
    """Combine two parents at a random point."""
    point = random.randint(1, CHROMOSOME_LENGTH - 1)
    child = parent_a[:point] + parent_b[point:]
    return child


def mutate(chromosome):
    """Flip each bit with a small probability."""
    child = chromosome[:]
    for index in range(len(child)):
        if random.random() < MUTATION_RATE:
            child[index] = 1 - child[index]
    return child


def genetic_algorithm():
    population = [make_chromosome() for _ in range(POPULATION_SIZE)]

    for generation in range(GENERATIONS):
        best = max(population, key=fitness)
        if generation % 10 == 0 or fitness(best) == CHROMOSOME_LENGTH:
            print(f"Generation {generation:2d}: best = {''.join(map(str, best))}, fitness = {fitness(best)}")
        if fitness(best) == CHROMOSOME_LENGTH:
            return best

        next_population = [best[:]]  # Keep the best solution (elitism).
        while len(next_population) < POPULATION_SIZE:
            parent_a = select_parent(population)
            parent_b = select_parent(population)
            child = crossover(parent_a, parent_b)
            next_population.append(mutate(child))
        population = next_population

    return max(population, key=fitness)


def main():
    random.seed(7)  # Reproducible output for a lab demonstration.
    best = genetic_algorithm()
    print("\nBest chromosome:", ''.join(map(str, best)))
    print("Fitness:", fitness(best), "/", CHROMOSOME_LENGTH)


if __name__ == "__main__":
    main()
