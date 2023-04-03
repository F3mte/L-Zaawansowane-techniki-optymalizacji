# Implementation of pseudocode for generating instances for
# Double Knapsack Problem (Chapter 5.3)
# Link:
# http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
from RandomNumberGenerator import RandomNumberGenerator

if __name__ == "__main__":

    # Step 0, initalization of used variables
    n, Z = 10, 15
    seed_gen = RandomNumberGenerator(Z)
    c_i = []
    w_i = []

    for i in range(n):
        c_i.append(seed_gen.nextInt(1, 30))
        w_i.append(seed_gen.nextInt(1, 30))
    B = seed_gen.nextInt(5*n, 10*n)

    # Print end results
    print(f"c_i: {c_i}")
    print(f"w_i: {w_i}")
    print(f"B: {B}")

    f = open(f"Data/dane_DescreteKnapsackProblem_n_{n}_Z_{Z}.dat", "w")
    f.write(f"n = {n};\n")
    f.write(f"c_i = {c_i};\n")
    f.write(f"w_i = {w_i};\n")
    f.write(f"B = {B};\n")
    f.close()
