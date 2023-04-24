# Implementation of TSP using B&B algorithm
# Travelling Salesman Problem (Problem 2.6)
# Link:
# http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
import numpy as np
import math

def tsp_bnb(cities):
    """
    Travelling Salesman Problem, using Branch and Bound method.
    """
    upper_bound = calculate_upper_bound(cities)
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
                    lower_bound = calculate_lower_bound(cities, n, path, city)
                    if lower_bound < best_tour[0] if best_tour is not None else math.inf and new_cost < upper_bound:
                        stack.append((new_cost, path + [city]))
        
    cost += cities[path[-1], 0]
    return best_tour

def calculate_lower_bound(cities, n, path, city):
    """
    Lower bound calculated using nearest neighbor heuristic,
    the idea is to always choose the nearest unvisited city as the next city to visit.
    """
    return sum(np.min(cities, axis=1)) + sum(np.min(cities, axis=0)[np.array(list(set(range(n)) - set(path)))]) + cities[path[-1], city]

def calculate_upper_bound(cities):
    """
    Upper bound calculated using nearest neighbor heuristic,
    the idea is to always choose the nearest unvisited city as the next city to visit.

    We need to find a tour that visits all cities once and returns to the starting city with the lowest possible cost.
    """
    n = len(cities)
    unvisited = set(range(1, n))
    current_city = 0
    tour = [0]

    while unvisited:
        next_city = min(unvisited, key=lambda city: cities[current_city][city])
        unvisited.remove(next_city)
        tour.append(next_city)

        current_city = next_city

    tour.append(0)
    cost = sum(cities[tour[i]][tour[i+1]] for i in range(n))
    return cost