# Implementation of pseudocode for generating instances for
# Permutation Flow Shop Problem (Chapter 2.8)
# Link:
# http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
from RandomNumberGenerator import RandomNumberGenerator


def generateFlowShopProblem(n: list, Z: list, dataNames: list):
    # Step 0, initalization of used variables
    for taskNumber, seedNumber in zip(n, Z):
        seed_gen = RandomNumberGenerator(seedNumber)
        p_1j = []
        p_2j = []
        p_3j = []

        for i in range(taskNumber):
            p_1j.append(seed_gen.nextInt(1, 99))
            p_2j.append(seed_gen.nextInt(1, 99))
            p_3j.append(seed_gen.nextInt(1, 99))

        dataNames.append(
            f"Data/dane_permutationFlowShopProblem_n_{taskNumber}_m_3_Z_{seedNumber}.dat")
        f = open(
            f"Data/dane_permutationFlowShopProblem_n_{taskNumber}_m_3_Z_{seedNumber}.dat", "w")
        f.write(f"{taskNumber} 3\n")
        for i in range(taskNumber):
            f.write(f"{p_1j[i]} ")
            f.write(f"{p_2j[i]} ")
            f.write(f"{p_3j[i]}\n")
        f.close()


if __name__ == "__main__":
    taskList = [10, 42, 100]
    seedList = [15, 42, 30]
    problemNames = []
    generateFlowShopProblem(taskList, seedList, problemNames)
    print(problemNames)
