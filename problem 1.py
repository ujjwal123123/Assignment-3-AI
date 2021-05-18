"""
Write a program (C/Python) to solve the 8-queen problem using stochastic hill
climbing search strategy. You should report the following for the search
strategy:
1) Demonstrate step-wise execution of the search strategy
2) The number of states/nodes generated/expanded
"""

"""
1) how many successors should be generated for each node? A total of 8! = 40320
   successors can be generated for any state.
2) How do we prevent revisits?
3) How to select fitness function?
"""

import random


def cost_function(placements):
    attacks = 0
    for i, val_i in enumerate(placements):
        for j, val_j in enumerate(placements):
            if j > i:
                if abs(i - j) == abs(val_i - val_j):
                    attacks += 1

    return attacks


def goal_test(placements):
    return cost_function(placements) == 0


def generate_successors(placements):
    """All the successors of `placements` with a lesser cost"""
    successors = []

    for i in range(8):
        for j in range(i, 8):
            new_successor = placements[:]
            new_successor[i], new_successor[j] = new_successor[j], new_successor[i]

            if cost_function(new_successor) <= cost_function(placements):
                successors.append((new_successor))

    if not successors:
        print("no successor found")
    return successors


def stochastic_hill_climbing():
    placements = [i for i in range(1, 9)]

    while True:
        successors = generate_successors(placements)

        for successor in successors:
            if goal_test(successor):
                return successor

        placements = random.choice(successors)


if __name__ == "__main__":
    print(stochastic_hill_climbing())
