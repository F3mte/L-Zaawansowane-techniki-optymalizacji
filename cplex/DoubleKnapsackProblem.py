from docplex.mp.model import Model

n = 10
B = 30
m = Model(name='descreteKnapsackProblem')

x = []
y = []
for i in range(0, n):
    x.append(m.binary_var(name='x{0}'.format(i)))
    y.append(m.binary_var(name='y{0}'.format(i)))

values = [1, 9, 8, 1, 5, 10, 8, 4, 7, 9]
weights1 = [10, 10, 2, 8, 6, 1, 1, 9, 10, 3]
weights2 = [4, 3, 2, 8, 9, 2, 3, 10, 4, 6]

val_of_knapsack_1 = m.sum(x[i]*values[i] for i in range(0, n))
val_of_knapsack_2 = m.sum(y[i]*values[i] for i in range(0, n))

m.maximize(m.add(val_of_knapsack_1, val_of_knapsack_2))

weight_of_knapsack1 = m.sum(x[i] for i in range(0, n))
weight_of_knapsack2 = m.sum(y[i] for i in range(0, n))
constraint1 = m.add(weight_of_knapsack1, weight_of_knapsack2)
constraint2 = m.sum(x[i]*weights1[i] for i in range(0, n))
constraint3 = m.sum(y[i]*weights2[i] for i in range(0, n))

m.add_constraint(constraint1 <= n)  # type: ignore
m.add_constraint(constraint2 <= B)  # type: ignore
m.add_constraint(constraint3 <= B)  # type: ignore

m.solve(log_output=True)
m.print_information()
m.print_solution()
