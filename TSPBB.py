# Implementation of TSP using B&B algorithm
# Travelling Salesman Problem (Problem 2.6)
# Link:
# http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
import numpy as np
import math

def tsp_bnb(cities, upper_bound=math.inf):
    """

    """
    n = len(cities)
    best_tour = None
    stack = [(0, [0])]
    while stack:
        (cost, path) = stack.pop()
        if len(path) == n:
            if best_tour is None or cost < best_tour[0]:
                best_tour = (cost, path)
        else:
            for city in range(n):
                if city not in path:
                    new_cost = cost + cities[path[-1], city]
                    lower_bound = sum(np.min(cities, axis=1)) + sum(np.min(cities, axis=0)[np.array(list(set(range(n)) - set(path)))]) + cities[path[-1], city]
                    if lower_bound < best_tour[0] if best_tour is not None else math.inf and new_cost < upper_bound:
                        stack.append((new_cost, path + [city]))
    return best_tour


# Example usage
cities = np.array([[0, 10, 15, 20],
                   [10, 0, 35, 25],
                   [15, 35, 0, 30],
                   [20, 25, 30, 0]])
best_tour = tsp_bnb(cities)
print("Best tour cost:", best_tour)
