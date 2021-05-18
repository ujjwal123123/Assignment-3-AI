"""
Write a program (C/Python) to solve the following problem using Genetic
Algorithm. You should report the following for the search strategy:
1) Demonstrate step-wise execution of the search strategy
2) The number of states/nodes generated/expanded
Problem: Maximize f(x) =2x^2 + 1, where 0<x<=6
"""


import random


def fitness_function(solution):
    if solution > 6 or solution < 0:
        return 0
    return 2 * (solution ** 2) + 1


def get_fitness(states: list):
    fitness_dict = dict()

    for state in states:
        fitness_dict[state] = fitness_function(state)

    return fitness_dict


def selection_operator(states: list) -> list:
    fitness_dict = get_fitness(states)

    sorted_by_fitness = [
        state
        for state, fitness in sorted(fitness_dict.items(), key=lambda item: -item[1])
    ]
    assert sorted_by_fitness is not None

    return list(zip(sorted_by_fitness[1::2], sorted_by_fitness[::2]))


def crossover_operator(pairs):
    new_states = []
    weight1 = 0.2
    weight2 = 0.8
    for pair in pairs:
        new_states.append(pair[0] * weight1 + pair[1] * weight2)
        new_states.append(pair[1] * weight1 + pair[0] * weight2)

    return new_states


def mutation_operator(states):
    for i in range(len(states)):
        if random.randint(1, 2) == 1:
            states[i] += 0.6
        elif states[i] > 0.1:
            states[i] -= 0.6


def genetic_algorithm():
    states = [0, 1, 2, 8]

    itr_no = 0
    while itr_no < 20:
        print("Initial states", states)

        itr_no += 1
        mutation_operator(states)
        pairs = selection_operator(states)
        states = crossover_operator(pairs)

        max_fitness = 0
        max_fitness_state = None

        for state in states:
            fitness = fitness_function(state)
            if fitness > max_fitness:
                max_fitness = fitness
                max_fitness_state = state

        print("Fitness", max_fitness, "State", max_fitness_state)


if __name__ == "__main__":
    genetic_algorithm()
