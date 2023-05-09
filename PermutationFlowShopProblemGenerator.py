# Implementation of pseudocode for generating instances for
# Permutation Flow Shop Problem (Chapter 2.8)
# Link:
# http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
from RandomNumberGenerator import RandomNumberGenerator

if __name__ == "__main__":

    # Step 0, initalization of used variables
    n, Z = 100, 30
    m = 3
    seed_gen = RandomNumberGenerator(Z)
    p_1j = []
    p_2j = []
    p_3j = []

    for i in range(n):
        p_1j.append(seed_gen.nextInt(1, 99))
        p_2j.append(seed_gen.nextInt(1, 99))
        p_3j.append(seed_gen.nextInt(1, 99))

    # Print end results
    print(f"p_1j: {p_1j}")
    print(f"p_2j: {p_2j}")
    print(f"p_3j: {p_3j}")

    f = open(f"Data/dane_permutationFlowShopProblem_n_{n}_m_3_Z_{Z}.dat", "w")
    f.write(f"{n} {m}\n")
    for i in range(n):  
        f.write(f"{p_1j[i]} ")
        f.write(f"{p_2j[i]} ")
        f.write(f"{p_3j[i]}\n")
    f.close()
