from docplex.mp.model import Model

n = 10
B = 63
m = Model(name='descreteKnapsackProblem')

x = []
for i in range(0, n):
    x.append(m.binary_var(name='x{0}'.format(i)))

values = [1, 11, 30, 22, 6, 23, 14, 25, 3, 23]
weights = [30, 27, 9, 6, 1, 24, 16, 29, 4, 1]

m.maximize(m.sum(x[i]*values[i] for i in range(0, n)))

constraint = m.sum(x[i]*weights[i] for i in range(0, n))

m.add_constraint(constraint <= B)  # type: ignore

m.solve(log_output=True)
m.print_information()
m.print_solution()
