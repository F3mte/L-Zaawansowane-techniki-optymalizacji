import numpy as np
import time
import matplotlib.pyplot as plt
from TSPBB import tsp_bnb

# Define the city arrays for each test
cities1 = np.array([[0, 10, 15, 20, 25], 
                    [10, 0, 32, 25, 20], 
                    [15, 32, 0, 30, 10], 
                    [20, 25, 30, 0, 32], 
                    [25, 20, 10, 32, 0]])

cities2 = np.array([[0, 20, 22, 28], 
                    [20, 0, 30, 34], 
                    [22, 30, 0, 12], 
                    [28, 34, 12, 0]])

cities3 = np.array([[0, 1, 2], 
                    [1, 0, 3], 
                    [2, 3, 0]])

cities4 = np.array([[0, 5, 2, 4], 
                    [5, 0, 3, 7], 
                    [2, 3, 0, 1], 
                    [4, 7, 1, 0]])

cities_list = [cities1, cities2, cities3, cities4]

execution_times = []

for cities in cities_list:
    start_time = time.time()
    tsp_bnb(cities)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

plt.plot(execution_times, 'o-')
plt.xlabel('Test Number')
plt.ylabel('Execution Time (s)')
plt.title('Execution Time for TSPBB')
plt.xticks(range(len(cities_list)), ['1', '2', '3', '4'])
plt.show()