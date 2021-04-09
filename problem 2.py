"""
Write a program (C/Python) to solve the following problem using Genetic
Algorithm. You should report the following for the search strategy:
1) Demonstrate step-wise execution of the search strategy
2) The number of states/nodes generated/expanded
Problem: Maximize f(x) =2x^2 + 1, where 0<x<=6
"""

"""
1) Which encoding should I use? Real valued or binary/integer?
2) How can I be sure that successors generated are not worse than parent?
"""

import random


def fitness_function(solution):
    return 2 * (solution ** 2) + 1


def get_fitness(states: list):
    fitness_dict = dict()

    for state in states:
        fitness_dict[state] = fitness_function(state)

    return fitness_dict


def selection_operator(fitness_dict: dict) -> list:
    # return pairs of integers sorted as per their fitness value
    print(fitness_dict.items())
    sorted_by_fitness = [
        state
        for state, fitness in sorted(fitness_dict.items(), key=lambda item: -item[1])
    ]
    # assert sorted_by_fitness is not None

    return list(zip(sorted_by_fitness[1::2], sorted_by_fitness[::2]))


def crossover_operator(pairs):
    """
    (5, 4) (3,2)
    (4.8, 4.2) (3.8, 3.2)
    """
    new_states = []
    a = 0.2
    b = 0.8  # 0.8
    for pair in pairs:
        new_states.append(pair[0] * a + pair[1] * b)
        new_states.append(pair[1] * a + pair[0] * b)

    return new_states


def mutation_operator(states):
    for i in range(len(states)):
        if random.randint(1, 2) == 1 and states[i] < 5.9:
            states[i] += 0.1
        elif states[i] > 0.1:
            states[i] -= 0.1


def genetic_algorithm():
    states = [0, 1, 2, 6]

    itr_no = 0
    while itr_no < 15:
        itr_no += 1
        pairs = selection_operator(get_fitness(states))
        states = crossover_operator(pairs)
        mutation_operator(states)

        print("Initial states", states)

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
