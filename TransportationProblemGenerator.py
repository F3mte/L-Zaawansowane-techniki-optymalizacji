# Implementation of pseudocode for generating instances for
# Transportation Problem (Chapter 2.2)
# Link:
# http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
from RandomNumberGenerator import RandomNumberGenerator


def pseudocodeStep3(K, seed):
    for i in range(K):
        S_i.append(seed.nextInt(1, 20))
        D_j = S_i.copy()
    return S_i, D_j


def pseudocodeStep4and5(seed, n, m, S_i, D_j):
    if n > m:
        for i in range(K, n):
            r = seed.nextInt(1, 20)
            S_i.append(r)
            j = seed.nextInt(1, m-1)
            D_j[j] += r
    elif m > n:
        for j in range(K, m):
            r = seed.nextInt(1, 20)
            D_j.append(r)
            i = seed.nextInt(1, n-1)
            S_i[i] += r
    return S_i, D_j


def pseudocodeStep6(seed, n, m):

    for i in range(n):
        for j in range(m):
            k_ij[i].append(seed.nextInt(1, 30))
    return k_ij


if __name__ == "__main__":

    # Step 0, initalization of used variables
    n, m, Z = 3, 4, 15
    S_i = []
    D_j = []
    k_ij = [[] for i in range(n)]

    # Step 1 and 2
    seed_gen = RandomNumberGenerator(Z)
    K = min(n, m)

    # Step3
    S_i, D_j = pseudocodeStep3(K, seed_gen)

    # Step 4 and 5
    S_i, D_j = pseudocodeStep4and5(seed_gen, n, m, S_i, D_j)

    # Step 6
    k_ij = pseudocodeStep6(seed_gen, n, m)

    # Print end results
    print(f"S_i: {S_i}")
    print(f"D_j: {D_j}")
    print(f"k_ij: {k_ij}")
