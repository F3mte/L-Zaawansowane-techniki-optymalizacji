import math
import time
import matplotlib.pyplot as plt


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
        self.best_cmax = self.calculate(self.neighbourhood_best_perm, self.matrix)
        neighbourhood_cmax = self.best_cmax
        self.best_cmax_list = [self.best_cmax]  # Store best Cmax values
        self.elapsed_time_list = [0.0]  # Store elapsed time values
        self.iteration_list = [0]  # Store iteration numbers

        do_loop = True
        start_time = time.process_time()
        iteration = 0

        while do_loop:
            neighbourhood_cmax = math.inf
            self.find_neigh_swap()  # Wygenruj sąsiedztwo
            for neigh_num in range(len(self.neighbourhood_list)):  # Znajdź sąsiedztwo z najlepszym czasem
                curr_cmax = self.calculate(self.neighbourhood_list[neigh_num], self.matrix)  # Oblicz czas dla obecnej permutacji
                if curr_cmax < neighbourhood_cmax:  # Jeśli czas jest lepszy, to zapamiętaj go razem z permutacją
                    neighbourhood_cmax = curr_cmax
                    self.neighbourhood_best_perm = self.neighbourhood_list[neigh_num].copy()
            if len(self.tabu_list) >= tabu_length:  # Wyrzuć najstarszy element z listy tabu, jeśli
                self.tabu_list.pop(0)
                self.tabu_list.append(self.neighbourhood_best_perm) # Dodaj najlepszą obecną permutację do listy tabu
            if neighbourhood_cmax < self.best_cmax: # Zapisz najlepszą znaną permutację i czas
                self.best_cmax = neighbourhood_cmax
                self.best_perm = self.neighbourhood_best_perm.copy()
            if stop == "time": # Warunek stopu: ilość czasu
                if time.process_time() - start_time > stop_value:
                    do_loop = False
                if stop == "iterate": # Warunek stopu: ilość iteracji
                    iteration += 1
                    elapsed_time = time.process_time() - start_time
                    self.best_cmax_list.append(self.best_cmax) # Store best Cmax values
                    self.elapsed_time_list.append(elapsed_time) # Store elapsed time values
                    self.iteration_list.append(iteration) # Store iteration numbers
                if iteration >= stop_value:
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
                    m[j] += table[i-1][j]  # Dla pierwszej maszyny dodaj czas przygotowania
                else:
                    m[j] = max(m[j], m[j-1]) + table[i-1][j]  # Dla kolejnych znajdź wg. wzoru 2.8 http://radoslaw.idzikowski.staff.iiar.pwr.wroc.pl/instruction/zto/problemy.pdf
        return max(m)

    def find_neigh_swap(self):
        """Funkcja szukajaca sasiedzctwa poprzez swap, zamienia dwa sasiednie elementy"""
        self.neighbourhood_list.clear()
        for i in range(len(self.neighbourhood_best_perm)-1):  # Zamień dwa sąsiadujące ze sobą zadania
            current_perm = self.neighbourhood_best_perm.copy()
            current_perm[i] = self.neighbourhood_best_perm[i+1]
            current_perm[i+1] = self.neighbourhood_best_perm[i]
            on_tabu_list = False
            for i in self.tabu_list:  # Sprawdź czy dana permutacja jest już na liście tabu
                if i == current_perm:
                    on_tabu_list = True
            if not on_tabu_list:  # Jeśli permutacji nie ma na liście tabu, dodaj ją do listy sąsiedztw
                self.neighbourhood_list.append(current_perm)

    def starting_perm(self):
        """Funkcja która zwraca permutacje w kolejności rosnącej"""
        perm = []
        for i in range(len(self.matrix)):
            perm.append(i+1)
        return perm
