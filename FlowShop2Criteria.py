import math
import time
import numpy as np
from PermutationFlowShopProblemGenerator import generateFlowShopProblem
import matplotlib.pyplot as plt
from Pareto import pareto_front


def read_from_file(file_name):
    """Odczytaj liczbę zadań, maszyn i czasy z pliku"""
    f = open(file_name, "r")

    line_from_file = f.readline()

    list_from_file = line_from_file.split(" ")
    number_of_task = int(list_from_file[0])
    number_of_machine = int(list_from_file[1])

    loaded_table_from_file = []

    for i in range(number_of_task):
        row = []
        line_from_file = f.readline()
        list_from_file = line_from_file.split(" ")
        for j in range(number_of_machine):
            row.append(int(list_from_file[j]))
        loaded_table_from_file.append(row)
    return loaded_table_from_file


class tabu_search:
    def __init__(self, task_lst, stop_value=10):
        """
    Funkcja wykonujaca tabusearch wraz z podanymi parametrami
    stop - pod jakim wzgledem zatrzymamy funkcje - albo po czasie albo po iteracjach
    stop_value - warunek stopu, gdy patrzymy na czas, jest to ilosc sekund, jesli patrzymy na iteracje - ilosc iteracji
    tabu_length - dlugosc listy tabu, ma wplyw na rozwiazanie, im dluzsza tym lepiej
    """
        self.matrix = task_lst
        self.best_perm = []
        self.neighbourhood_list = []
        self.best_cmax = math.inf
        self.best_sum = math.inf
        self.neighbourhood_best_perm = []
        self.best_cmax_list = [0]  # Lista do stworzenia wykresu
        self.elapsed_time_list = [0.0]  # Lista do stworzenia wykresu
        self.start_time = time.process_time()
        self.iteration_list = [0]
        self.dominating_cmax = []
        self.dominating_sum = []
        self.stop_value = stop_value

    def execute(self, stop="iterate", tabu_length=10):
        self.best_perm = self.starting_perm()
        self.neighbourhood_best_perm = self.best_perm
        self.best_cmax, _ = self.calculate(
            self.neighbourhood_best_perm, self.matrix)
        neighbourhood_cmax = self.best_cmax

        do_loop = True

        if stop == "time":
            stop_param = time.process_time()
        elif stop == "iterate":
            stop_param = 0
        else:
            print("ERROR: execute option not known")
        while do_loop:
            neighbourhood_cmax = math.inf
            neighbourhood_sum = math.inf
            self.find_neigh_swap()  # Wygenruj sąsiedztwo
            # Znajdź sąsiedztwo z najlepszym czasem
            for neigh_num in range(len(self.neighbourhood_list)):
                curr_cmax, curr_sum = self.calculate(
                    self.neighbourhood_list[neigh_num], self.matrix)  # Oblicz czas dla obecnej permutacji
                # Jeśli nowe sąsiedztwo dominuje poprzednie to je dodaj do zbioru rozwiązań 🥺
                if (curr_cmax < neighbourhood_cmax and curr_sum <= neighbourhood_sum) \
                        or (curr_cmax <= neighbourhood_cmax and curr_sum < neighbourhood_sum):
                    neighbourhood_cmax = curr_cmax
                    neighbourhood_sum = curr_sum
                    self.dominating_cmax.append(curr_cmax)
                    self.dominating_sum.append(curr_sum)
                    self.neighbourhood_best_perm = self.neighbourhood_list[neigh_num].copy(
                    )
                else:
                    if (np.random.random() < 0.5):
                        neighbourhood_cmax = curr_cmax
                        neighbourhood_sum = curr_sum
                        self.dominating_cmax.append(curr_cmax)
                        self.dominating_sum.append(curr_sum)
                        self.neighbourhood_best_perm = self.neighbourhood_list[neigh_num].copy(
                        )
            # Dodaj najlepszą obecną permutację do listy tabu
            if (neighbourhood_cmax <= self.best_cmax and neighbourhood_sum < self.best_sum) \
                    or (neighbourhood_cmax < self.best_cmax and neighbourhood_sum <= self.best_sum):  # Zapisz najlepszą znaną permutację i czas
                self.best_cmax = neighbourhood_cmax
                self.best_sum = neighbourhood_sum
                self.best_perm = self.neighbourhood_best_perm.copy()
            if stop == "time":  # Warunek stopu: ilość czasu
                if time.process_time() - stop_param > self.stop_value:
                    do_loop = False
            if stop == "iterate":  # Warunek stopu: ilość iteracji
                stop_param += 1
                elapsed_time = time.process_time() - self.start_time
                # Dodaj do listy najlepszych wyników po każdej iteracji
                self.best_cmax_list.append(self.best_cmax)
                # Dodaj do listy czasu po każdej iteracji
                self.elapsed_time_list.append(elapsed_time)
                self.iteration_list.append(stop_param)
                if stop_param > self.stop_value:
                    do_loop = False

    def calculate(self, permutation, table):
        """
    permutation - konkretna kolejnosc zadan do realizacji,
    table - oryginalna tablica, nie uporzadkowana, jest to wazne, bo w kilku miejscach poslugujemy sie uporzadkowanna
    """
        m = [0] * len(table[0])
        for i in permutation:  # Dla każdego zadania z danej permutacji
            for j in range(0, len(table[0])):  # Dla każdej maszyny
                if j == 0:
                    # Dla pierwszej maszyny dodaj czas przygotowania
                    m[j] += table[i-1][j]
                else:
                    # Dla kolejnych znajdź wg. wzoru 2.8 http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
                    m[j] = max(m[j], m[j-1]) + table[i-1][j]
        return max(m), sum(m)

    def find_neigh_swap(self):
        """Funkcja szukajaca sasiedzctwa poprzez swap, zamienia dwa sasiednie elementy"""
        self.neighbourhood_list.clear()
        # Zamień dwa sąsiadujące ze sobą zadania
        for i in range(len(self.neighbourhood_best_perm)-1):
            current_perm = self.neighbourhood_best_perm.copy()
            current_perm[i] = self.neighbourhood_best_perm[i+1]
            current_perm[i+1] = self.neighbourhood_best_perm[i]
            self.neighbourhood_list.append(current_perm)

    def starting_perm(self):
        """Funkcja która zwraca permutacje w kolejności rosnącej"""
        perm = []
        for i in range(len(self.matrix)):
            perm.append(i+1)
        return perm


if __name__ == "__main__":
    numberOfTasks = [30]
    listOfSeeds = [42]
    listOfData = []
    iter_values = [10, 30, 50, 100, 200, 300]
    # Wygeneruj instancje
    generateFlowShopProblem(numberOfTasks, listOfSeeds,
                            listOfData)
    # Wykonaj tabu search dla każdej instancji
    best_cmax_values = []
    elapsed_time_values = []
    all_cmax_values = []
    iteration_list = []
    cmax_list = []
    sum_list = []
    tuple_of_criterias = []
    for data in listOfData:
        for iterations in iter_values:
            matrix = read_from_file(data)
            # Stwórz klasę
            tabu = tabu_search(matrix, stop_value=iterations)
            # Wykonaj tabu search
            tabu.execute()
            # Zapisz wyniki
            best_cmax_values.append(tabu.best_cmax)
            elapsed_time_values.append(tabu.elapsed_time_list[-1])
            all_cmax_values.append(tabu.best_cmax_list)
            iteration_list.append(tabu.iteration_list)
            cmax_list = tabu.dominating_cmax
            sum_list = tabu.dominating_sum
            tuple_of_criterias.append(list(zip(cmax_list, sum_list)))
            # print(tabu.best_cmax)
            # print(tabu.best_perm)
            # print(tabu.best_cmax_list)
            # print(tabu.elapsed_time_list)
    for points in tuple_of_criterias:
        pareto_x, pareto_y = pareto_front(points)

        x = [p[0] for p in points]
        y = [p[1] for p in points]

        x = np.array(x)
        y = np.array(y)

        plt.scatter(x, y, color='blue', label='Punkty')
        plt.plot(pareto_x, pareto_y, color='red', label='Front Pareto')
        plt.scatter(pareto_x, pareto_y, color='red')
        plt.xlabel('Kryterium 1')
        plt.ylabel('Kryterium 2')
        plt.title(f'Front Pareto')
        plt.legend()
        plt.grid(True)
        plt.show()
    # Pokaż wyniki na wykresach
    # plt.figure(figsize=(10, 6))
    # plt.subplot(2, 1, 1)
    # print(all_cmax_values)
    # print(iteration_list)
    # print(numberOfTasks[0])
    # plt.plot(iteration_list[0], all_cmax_values[0],
    #  marker='o', linestyle='-', color='b')
    # plt.plot(iteration_list[1], all_cmax_values[1],
    #  marker='o', linestyle='-', color='b')
    # plt.plot(iteration_list[2], all_cmax_values[2],
    #  marker='o', linestyle='-', color='b')
    # plt.xlabel('Number of iteration')
    # plt.ylabel('Best Cmax')
    # plt.title('Best Cmax vs Number of instances')

    # plt.subplot(2, 1, 2)
    # plt.plot(numberOfTasks, elapsed_time_values,
    #  marker='o', linestyle='-', color='r')
    # plt.xlabel('Run')
    # plt.ylabel('Elapsed Time (s)')
    # plt.title('Elapsed Time vs Run')

    # plt.tight_layout()
    # plt.show()
