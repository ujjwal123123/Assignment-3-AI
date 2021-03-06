"""
Write a program (C/Python) to solve the following problem using Particle Swarm
Optimization. You should report the following for the search strategy:

  a) Demonstrate step-wise execution of the search strategy
  b) The number of states/nodes generated/expanded

Problem: Divide the N students in k groups based on their marks in AI such as
diversity in each group is minimized.
"""

import random
from numpy import array


def find_closest(numbers: list, closest_to: int):
    closest = None  # int, position for which squared distance is least

    # find nearest centroid to mark. We need to minimize the cost.
    for num in numbers:
        if closest is None or abs(closest_to - num) < abs(closest_to - closest):
            closest = num

    return closest


class particle:
    # TODO: set these parameters correctly
    INERTIA = 0.5
    CONST1 = 0.01
    CONST2 = 0.01

    def __init__(self, cluster_count: int, min_marks: int, max_marks):
        self.velocity = array([0] * cluster_count)  # array of numbers
        self.centroids = array(
            sorted([random.uniform(min_marks, max_marks) for _ in range(cluster_count)])
        )  # intialise with random data

        self.local_best_centroids = None  # list, Analogous to position in usual PSO
        self.local_best_cost = None  # int

    def calculate_cost(self, marks: list):
        """Update particle_best and global_best"""
        # find squared distance of each particle to the nearest representative
        # in `particle_positions`

        particle_cost_value = 0

        for mark in marks:
            closet_centroid = find_closest(
                self.centroids, mark
            )  # int, centroid for which squared distance is least

            particle_cost_value += (closet_centroid - mark) ** 2

        if self.local_best_cost is None or self.local_best_cost > particle_cost_value:
            self.local_best_cost = particle_cost_value
            self.local_best_centroids = self.centroids

        assert (
            self.local_best_centroids is not None and self.local_best_cost is not None
        )

    def move(self, global_best_centroids):
        self.velocity = (
            self.velocity * self.INERTIA
            + (self.local_best_centroids - self.centroids) * self.CONST1
            + (global_best_centroids - self.centroids) * self.CONST2
        )
        self.centroids += self.velocity


class particle_swarm_optimization:
    """To divide `N` students in `cluster_count` groups using marks they
    obtained. Marks are represented using `marks` list."""

    ITERATION_COUNT = 10
    PARTICLE_COUNT = 10  # no of particles

    def __init__(self, cluster_count: int, marks: list):
        self.cluster_count = cluster_count
        self.marks = sorted(marks)
        self.global_best_centroids = None
        self.global_best_cost = None
        self.particles = [
            particle(cluster_count, min(marks), max(marks))
            for _ in range(self.PARTICLE_COUNT)
        ]
        self.cost()

    def cost(self):
        for particle in self.particles:
            particle.calculate_cost(self.marks)

            if (
                self.global_best_cost is None
                or self.global_best_cost > particle.local_best_cost
            ):
                self.global_best_cost = particle.local_best_cost
                self.global_best_centroids = particle.local_best_centroids

            assert (
                self.global_best_centroids is not None
                and self.global_best_cost is not None
            )

    def move(self):
        for particle in self.particles:
            particle.move(self.global_best_centroids)

    def solve(self):
        for _ in range(self.ITERATION_COUNT):
            self.move()
            self.cost()

        print(self.global_best_centroids)
        print(self.global_best_cost)

        self.make_groups()

    def make_groups(self):
        groups_dict = dict()  # map centroids to marks (centroid : [marks])
        for mark in self.marks:
            closest = find_closest(self.global_best_centroids, mark)

            if closest in groups_dict:
                groups_dict[closest].append(mark)
            else:
                groups_dict[closest] = [mark]

        result = []
        for group in groups_dict.values():
            result.append(group)

        print(result)


if __name__ == "__main__":
    problem = particle_swarm_optimization(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    problem.solve()
