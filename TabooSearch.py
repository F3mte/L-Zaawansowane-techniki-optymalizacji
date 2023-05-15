import math
import time


def calculate(permutation, table):
    """
# permutation - konkretna kolejnosc zadan do realizacji,
# table - oryginalna tablica, nie uporzadkowana, jest to wazne, bo w kilku miejscach poslugujemy sie uporzadkowanna
# table[][]
# example index
# table[current_number_of_machine][current_number_of_task]
"""
    m = [0] * len(table[0])  # robienie miejsca listę
    for i in permutation:
        for j in range(0, len(table[0])):  # inaczej ilosc maszyn
            if j == 0:
                # i-1 bo w wektorze permutacji mamy liczby od 1 i bysmy wyleciali poza tablice
                m[j] += table[i-1][j]
            else:
                m[j] = max(m[j], m[j-1]) + table[i-1][j]
    return max(m)


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
    return number_of_task, number_of_machine, loaded_table_from_file


class tabu_search:
    def __init__(self, task_lst):
        """
    Funkcja wykonujaca tabusearch wraz z podanymi parametrami
    neighbourhood - jaka opcja do szukania sasiedzctwa , swap czy insert
    stop - pod jakim wzgledem zatrzymamy funkcje - albo po czasie albo po iteracjach
    stop_value - warunek stopu, gdy patrzymy na czas, jest to ilosc sekund, jesli patrzymy na iteracje - ilosc iteracji
    tabu_length - dlugosc listy tabu, ma wplyw na rozwiazanie, im dluzsza tym lepiej
    """
        self.matrix = task_lst
        self.best_perm = []
        self.tabu_list = []
        self.neighbourhood_list = []
        self.best_cmax = math.inf
        self.neighbourhood_best_perm = []

    def execute(self, stop="iterate", stop_value=10, tabu_length=10):
        self.best_perm = self.starting_perm()
        self.neighbourhood_best_perm = self.best_perm
        self.best_cmax = calculate(
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
            self.find_neigh_swap()
            for neigh_num in range(len(self.neighbourhood_list)):
                curr_cmax = calculate(
                    self.neighbourhood_list[neigh_num], self.matrix)
                if curr_cmax < neighbourhood_cmax:
                    neighbourhood_cmax = curr_cmax
                    self.neighbourhood_best_perm = self.neighbourhood_list[neigh_num].copy(
                    )
            if len(self.tabu_list) >= tabu_length:
                self.tabu_list.pop(0)
            self.tabu_list.append(self.neighbourhood_best_perm)
            if neighbourhood_cmax < self.best_cmax:
                self.best_cmax = neighbourhood_cmax
                self.best_perm = self.neighbourhood_best_perm.copy()
            if stop == "time":
                if time.process_time() - stop_param > stop_value:
                    do_loop = False
            if stop == "iterate":
                stop_param += 1
                if stop_param > stop_value:
                    do_loop = False

    def find_neigh_swap(self):
        """funkcja szukajaca sasiedzctwa poprzez swap, zamienia dwa sasiednie elementy"""
        self.neighbourhood_list.clear()
        for i in range(len(self.neighbourhood_best_perm)-1):
            current_perm = self.neighbourhood_best_perm.copy()
            current_perm[i] = self.neighbourhood_best_perm[i+1]
            current_perm[i+1] = self.neighbourhood_best_perm[i]
            on_tabu_list = False
            for i in self.tabu_list:  # zabezpieczenie przed wpisywaniem czegos do tabu list, jesli bylo juz przedtem
                if i == current_perm:
                    on_tabu_list = True
            if on_tabu_list == False:
                self.neighbourhood_list.append(current_perm)

    def starting_perm(self):
        """funkcja która zwraca permutacje w kolejności rosnącej"""
        perm = []
        for i in range(len(self.matrix)):
            perm.append(i+1)
        return perm


if __name__ == "__main__":
    numberOfTask, numberOfMachine, matrix = read_from_file(
        "Data\\dane_permutationFlowShopProblem_n_10_m_3_Z_15.dat")
    tabu = tabu_search(matrix)
    tabu.execute()
    print(tabu.best_cmax)
    print(tabu.best_perm)
