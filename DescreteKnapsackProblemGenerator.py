# Implementation of pseudocode for generating instances for
# Double Knapsack Problem (Chapter 5.3)
# Link:
# http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
from RandomNumberGenerator import RandomNumberGenerator


def generateKnapsackProblemData(n_input, Z_input, problemNames):
    # Step 0, initalization of used variables
    for n, Z in zip(n_input, Z_input):
        seed_gen = RandomNumberGenerator(Z)
        c_i = []
        w_i = []

        for i in range(n):
            c_i.append(seed_gen.nextInt(1, 30))
            w_i.append(seed_gen.nextInt(1, 30))
        B = seed_gen.nextInt(5*n, 10*n)

        filename = f"Data/dane_DescreteKnapsackProblem_n_{n}_Z_{Z}.dat"
        problemNames.append(filename)
        f = open(filename, "w")
        f.write(f"{B}\n")
        f.write(f"{n}\n")
        for i in range(n):
            f.write(f"{c_i[i]}\n")
        for i in range(n):
            f.write(f"{w_i[i]}\n")
        f.close()


if __name__ == "__main__":
    length = [10, 42, 100]
    seedList = [15, 42, 30]
    problemNames = []
    generateKnapsackProblemData(length, seedList, problemNames)
    print(problemNames)
