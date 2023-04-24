# Implementation of pseudocode for generating instances for
# Scheduling on a single machine with total weighted tardiness (Chapter 2.7)
# Link:
# http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
from RandomNumberGenerator import RandomNumberGenerator

if __name__ == "__main__":

    # Step 0, initalization of used variables
    n, Z = 100, 30
    seed_gen = RandomNumberGenerator(Z)
    p_i = []
    w_i = []

    for i in range(n):
        p_i.append(seed_gen.nextInt(1, 30))
        w_i.append(seed_gen.nextInt(1, 30))

    S = sum(p_i)

    # Print end results
    print(f"p_i: {p_i}")
    print(f"w_i: {w_i}")
    print(f"S: {S}")

    f = open(f"Data/dane_SchedulingOnSingleMachine_n_{n}_Z_{Z}.dat", "w")
    f.write(f"p_i = {p_i}\n")
    f.write(f"w_i = {w_i}\n")
    f.write(f"S = {S}")
    f.close()
