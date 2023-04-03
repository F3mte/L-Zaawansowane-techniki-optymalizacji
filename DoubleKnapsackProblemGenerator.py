# Implementation of pseudocode for generating instances for
# Discrete Knapsack Problem (Chapter 2.5)
# Link:
# http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
from RandomNumberGenerator import RandomNumberGenerator

if __name__ == "__main__":

    # Step 0, initalization of used variables
    n, Z = 100, 30
    seed_gen = RandomNumberGenerator(Z)
    c_i = []
    w_i = []
    v_i = []

    for i in range(n):
        c_i.append(seed_gen.nextInt(1, 10))
        w_i.append(seed_gen.nextInt(1, 10))
        v_i.append(seed_gen.nextInt(1, 10))
    B = seed_gen.nextInt(n, 4*n)

    # Print end results
    print(f"c_i: {c_i}")
    print(f"w_i: {w_i}")
    print(f"v_i: {v_i}")
    print(f"B: {B}")

    f = open(f"Data/dane_DoubleKnapsackProblem_n_{n}_Z_{Z}.dat", "w")
    f.write(f"n = {n};\n")
    f.write(f"c_i = {c_i};\n")
    f.write(f"w_i = {w_i};\n")
    f.write(f"v_i = {v_i};\n")
    f.write(f"B = {B};\n")
    f.close()
