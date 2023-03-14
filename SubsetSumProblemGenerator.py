# Implementation of pseudocode for generating instances for
# Subset Sum Problem (Chapter 2.1)
# Link:
# http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
from RandomNumberGenerator import RandomNumberGenerator

if __name__ == "__main__":

    # Step 0, initalization of used variables
    n, Z = 42, 42
    seed_gen = RandomNumberGenerator(Z)
    T = seed_gen.nextInt(-50*n, 50*n)
    S_i = []

    for i in range(n):
        S_i.append(seed_gen.nextInt(-100, 100))

    # Print end results
    print(f"S_i: {S_i}")
    print(f"T: {T}")

    f = open(f"Data/dane_subsetsumproblem_n_{n}_Z_{Z}.dat", "w")
    f.write(f"T = {T};\n")
    f.write(f"S_i = {S_i};")
    f.close()
