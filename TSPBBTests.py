import time
import matplotlib.pyplot as plt
from TravellingSalesmanProblemGenerator import cities_gen
from TSPBB import tsp_bnb
from TSPBS import tsp_bs

cities1 = cities_gen(4, 30)

cities2 = cities_gen(5, 30)

cities3 = cities_gen(6, 30)

cities4 = cities_gen(7, 30)

cities_list = [cities1, cities2, cities3, cities4]

execution_times_bnb = []

for cities in cities_list:
    start_time = time.time()
    best_tour = tsp_bnb(cities)
    print(best_tour)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times_bnb.append(execution_time)

# plt.plot(execution_times_bnb, 'o-')
# plt.xlabel('Test Number')
# plt.ylabel('Execution Time (s)')
# plt.title('Execution Time for TSPBB')
# plt.xticks(range(len(cities_list)), ['1', '2', '3', '4'])
# plt.show()

execution_times_bs = []

for cities in cities_list:
    start_time = time.time()
    best_tour = tsp_bs(cities)
    print(best_tour, 5)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times_bs.append(execution_time)

plt.plot(execution_times_bs, 'o-')
plt.plot(execution_times_bnb, '--')
plt.xlabel('Test Number')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time')
plt.xticks(range(len(cities_list)), ['1', '2', '3', '4'])
plt.show()