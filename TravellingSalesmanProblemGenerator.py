# Implementation of pseudocode for generating instances for
# Travelling Salesman Problem (Chapter 2.6)
# Link:
# http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
from RandomNumberGenerator import RandomNumberGenerator
import numpy as np

def main(n, Z):
    return cities_gen(n, Z)

def cities_gen(n, Z):

    seed_gen = RandomNumberGenerator(Z)
    cities = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if i != j:
                cities[i, j] = seed_gen.nextInt(1, 30)
                cities[j, i] = cities[i, j]
    return cities

if __name__ == "__main__":
    main()
