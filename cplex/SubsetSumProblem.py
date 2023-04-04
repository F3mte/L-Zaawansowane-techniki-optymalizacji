from docplex.mp.model import Model
import time
# import matplotlib.pyplot as plt
# import numpy as np

list_of_data = [
    [
        10,
        -500,
        [95, -33, 76, 99, -43, 41, -64, -62, -96, 51]
    ],
    [
        42,
        -2099,
        [5, 47, -48, -25, -61, 96, 2, 6, -49, -79, 63, 81, -10, -51, -51, -63, -36, -80, 62, 7, 69, 48, -85, 8, -74, 73, -7, -6, -10, -54, -98, -96, 99, 84, 57, 14, 54, 25, -31, -25, -47, -30]
    ],
    [
        100,
        -4998,
        [90, 34, 52, 97, 14, -18, -27, -24, -92, 1, 17, 86, -93, 21, 79, -73, -54, 0, -99, 5, 21, 34, 83, -23, 62, 52, 24, -4, -93, -38, 74, 75, -15, -84, 70, 96, 39, 46, 92, -18, -5, 36, 20, 9, -64, 90, 8, -64, -82, 99, -34, -74, -51, 56, 100, 19, 86, -45, 64, -72, -73, -2, 14, 20, 64, 97, 45, -13, -58, -96, 5, -38, -17, 79, 87, -54, 1, 69, -79, 67, 52, -5, 31, -91, 78, -83, 53, 97, 32, 100, -62, 6, -20, 47, -24, -28, -51, -85, -8, -77]
    ]
]

number_of_n = []
solving_time = []

for data in list_of_data:
    n = data[0]
    T = data[1]
    values = data[2]
    m = Model(name='subsetsumProblem')

    x = []
    for i in range(0, n):
        x.append(m.binary_var(name='x{0}'.format(i)))

    m.minimize(T - m.sum(x[i]*values[i] for i in range(0, n)))  # type: ignore

    start = time.time()
    m.solve(log_output=True)
    end = time.time()

    m.print_information()
    m.print_solution()

    number_of_n.append(data[0])
    solving_time.append(end - start)

for index, n in enumerate(number_of_n):
    print(f"Czas rozwiązywania dla n={n}: {solving_time[index]:.3f}")

# fig, ax = plt.subplots()
# ax.plot(number_of_n, solving_time)
# plt.show()
