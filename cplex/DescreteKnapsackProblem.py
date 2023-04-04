from docplex.mp.model import Model
import time

list_of_data = [
    [
        10,
        63,
        [1, 11, 30, 22, 6, 23, 14, 25, 3, 23],
        [30, 27, 9, 6, 1, 24, 16, 29, 4, 1]
    ],
    [
        42,
        308,
        [1, 23, 12, 30, 16, 4, 28, 8, 6, 4, 17, 23, 17, 26, 15, 8, 1, 28, 18, 19, 12, 11, 11, 16, 14, 6, 30, 3, 14, 6, 30, 21, 14, 6, 25, 1, 20, 8, 16, 30, 24, 20],
        [16, 8, 6, 16, 8, 25, 14, 8, 10, 25, 26, 3, 4, 14, 14, 1, 30, 24, 24, 11, 9, 20, 2, 5, 10, 2, 17, 30, 22, 17, 6, 12, 23, 25, 3, 5, 12, 16, 4, 11, 8, 28]
    ],
    [
        100,
        835,
        [1, 21, 30, 13, 12, 16, 28, 19, 5, 16, 16, 21, 12, 23, 15, 10, 27, 3, 30, 22, 13, 21, 17, 29, 6, 30, 4, 24, 18, 9, 5, 15, 18, 30, 13, 1, 10, 27, 7, 26, 26, 15, 2, 3, 30, 30, 16, 23, 11, 3, 4, 19, 19, 3, 2, 20, 20, 23, 24, 14, 22, 3, 25, 5, 13, 19, 16, 18, 30, 19, 22, 21, 15, 8, 17, 28, 24, 18, 25, 20, 14, 21, 26, 24, 13, 29, 23, 4, 18, 15, 15, 9, 17, 12, 16, 5, 1, 21, 17, 6],
        [29, 23, 18, 11, 2, 18, 2, 27, 7, 1, 19, 28, 25, 19, 2, 26, 13, 26, 21, 29, 15, 19, 6, 17, 3, 10, 8, 30, 28, 25, 5, 18, 25, 22, 7, 16, 13, 29, 16, 4, 23, 20, 27, 23, 20, 6, 12, 12, 8, 14, 2, 11, 5, 30, 29, 14, 22, 8, 12, 28, 8, 13, 9, 6, 16, 17, 14, 19, 13, 12, 20, 14, 8, 29, 20, 25, 30, 27, 17, 3, 9, 3, 2, 8, 10, 18, 26, 29, 2, 20, 18, 29, 14, 9, 25, 6, 16, 27, 30, 23]
    ]
]

number_of_n = []
solving_time = []

for data in list_of_data:
    n = data[0]
    B = data[1]
    values = data[2]
    weights = data[3]
    m = Model(name='descreteKnapsackProblem')

    x = []
    for i in range(0, n):
        x.append(m.binary_var(name='x{0}'.format(i)))

    constraint = m.sum(x[i]*weights[i] for i in range(0, n))
    m.add_constraint(constraint <= B)  # type: ignore

    m.maximize(m.sum(x[i]*values[i] for i in range(0, n)))

    start = time.time()
    m.solve(log_output=True)
    end = time.time()

    m.print_information()
    m.print_solution()

    number_of_n.append(data[0])
    solving_time.append(end - start)

for index, n in enumerate(number_of_n):
    print(f"Czas rozwiązywania dla n={n}: {solving_time[index]:.3f}")
