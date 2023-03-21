# Implementation of pseudocode for generating instances for
# Quadratic Assignment Problem (Chapter 2.4)
# Link:
# http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
from RandomNumberGenerator import RandomNumberGenerator

if __name__ == "__main__":

    # Step 0, initalization of used variables
    n, Z = 100, 30
    seed_gen = RandomNumberGenerator(Z)
    w_ij = []
    d_ij = []

    for i in range(n):
        w_ij.append(seed_gen.nextInt(1, 50))
        d_ij.append(seed_gen.nextInt(1, 50))

    # Print end results
    print(f"w_ij: {w_ij}")
    print(f"d_ij: {d_ij}")

    f = open(f"Data/dane_quadraticAssignmentProblem_n_{n}_Z_{Z}.dat", "w")
    f.write(f"n = {n};\n")
    f.write(f"w_ij = {w_ij};\n")
    f.write(f"d_ij = {d_ij};")
    f.close()
