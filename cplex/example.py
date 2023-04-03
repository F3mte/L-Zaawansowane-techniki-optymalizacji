from docplex.mp.model import Model

n = 10
T = -500
m = Model(name='sumProblem')

x = []
for i in range(0, n):
    x.append(m.binary_var(name='x{0}'.format(i)))

values = [95, -33, 76, 99, -43, 41, -64, -52, 96, 51]

total = m.sum(x[i]*values[i] for i in range(0, n))

m.minimize(m.abs(T-total))  # type: ignore

m.solve(log_output=True)
m.print_information()
m.print_solution()
