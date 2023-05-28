import time
import numpy as np
import matplotlib.pyplot as plt
from DescreteKnapsackProblemGenerator import generateKnapsackProblemData


def read_from_file(file_name):
    """Odczytaj liczbę zadań, maszyn i czasy z pliku"""
    f = open(file_name, "r")
    valueOfItems = []
    weightOfItems = []

    backpackSize = int(f.readline().rstrip('\n'))
    numberOfItems = int(f.readline().rstrip('\n'))
    for i in range(numberOfItems):
        valueOfItems.append(int(f.readline().rstrip('\n')))
    for i in range(numberOfItems):
        weightOfItems.append(int(f.readline().rstrip('\n')))

    return backpackSize, numberOfItems, valueOfItems, weightOfItems


class Chromosome:
    """Class to manage individual chromosomes in genetic algorithm.
    """

    def __init__(self, weights, profits, knapsack_size) -> None:
        # Lista wag kolejnych przedmiotów
        self.weights = weights
        # Lista wartości kolejnych przedmiotów
        self.profits = profits
        self.knapsack_size = knapsack_size                  # Pojemność plecaka
        # Lista z binarnymi zmiennymi decyzyjnymi (geny)
        self.genes = np.random.randint(0, 2, len(weights))
        # Długość łańcucha genów
        self.size = len(self.genes)

    @property
    def fitness(self):
        """Wartość funkcji dopasowania"""
        total_weight = np.dot(self.genes, self.weights)
        fitness = np.dot(self.genes, self.profits)
        if total_weight <= self.knapsack_size:
            return fitness
        return 0

    def __lt__(self, o: object) -> bool:
        """Używane przy operacji sortowania"""
        return self.fitness > o.fitness

    def __eq__(self, o: object) -> bool:
        """Używane przy operacji sortowania"""
        return self.fitness == o.fitness

    def __gt__(self, o: object) -> bool:
        """Używane przy operacji sortowania"""
        return self.fitness < o.fitness

    def single_point_crossover(self, chromosome):
        """Wybierz losowo jeden punkt wobec którego będzie dokonane krzyżowanie"""
        crossover_point = np.random.randint(1, self.size - 1)
        offspring1 = Chromosome(self.weights, self.profits, self.knapsack_size)
        offspring1.genes = np.concatenate(
            (self.genes[:crossover_point], chromosome.genes[crossover_point:]))
        offspring2 = Chromosome(self.weights, self.profits, self.knapsack_size)
        offspring2.genes = np.concatenate(
            (chromosome.genes[:crossover_point], self.genes[crossover_point:]))
        return offspring1, offspring2

    def mutate(self, mutation_probability):
        """Jeśli wylosowana wartość jest mniejsza niż 'mutation_probability' to dokonaj mutacji"""
        self.genes = np.where(
            np.random.random(self.size) < mutation_probability, self.genes ^ 1,
            self.genes)


class GeneticAlgorithm:
    """Class to manage genetic algorithm for 0/1 Knapsack problem.
    """

    def __init__(self,
                 weights,
                 profits,
                 knapsack_size,
                 population_size,
                 selection_ratio=0.5,
                 mutation_prob=0.05) -> None:
        self.weights = weights
        self.profits = profits
        self.knapsack_size = knapsack_size
        self.population_size = population_size
        self.selection_ratio = selection_ratio
        self.mutation_prob = mutation_prob
        self.chromosomes = sorted([
            Chromosome(self.weights, self.profits, self.knapsack_size)
            for i in range(population_size)
        ])
        self.max_profit = []

    def crossover(self, parents):
        """Dokonaj krzyżowania"""
        return parents[0].single_point_crossover(parents[1])

    def mutatation(self, offsprings, mutation_prob):
        """Daj każdemu osobnikowi szanse na mutacje"""
        for offspring in offsprings:
            offspring.mutate(mutation_prob)
        return offsprings

    def next_generation(self):
        """Stwórz kolejne pokolenie, kolejno:
        - wybierz lepiej dostosowaną część,
        - wybierz rodziców i dokonaj krzyżowania,
        - dokonaj losowo mutacji osobników,
        - posortuj powstałą populację
        """
        # Wybierz część populacji, upewnij się, że liczba będzie parzysta
        n_selection = int(self.population_size * self.selection_ratio)
        n_selection = (n_selection // 2) * 2
        fittest_individuals = self.chromosomes[:n_selection]

        # Operacja krzyżowania dla kolejnych par rodziców
        offsprings = []
        for i in range(0, n_selection, 2):
            offsprings += self.crossover(fittest_individuals[i:i + 2])

        # Mutacja losowych osobników
        offsprings = self.mutatation(offsprings, self.mutation_prob)

        # Dodaj powstałą populacją do istniejącej
        self.chromosomes += offsprings
        self.chromosomes = sorted(self.chromosomes)[:self.population_size]

    def fittest_chromosome(self):
        return self.chromosomes[0]

    def evolve(self, generations, log_freq=1000):
        """Główna pętla algorytmu"""
        for generation in range(generations):
            ga.next_generation()
            self.max_profit.append(self.fittest_chromosome().fitness)
            if generation % log_freq == 0:
                print(
                    f'Generation {generation+1}: Max Profit = {self.max_profit[generation]}')
            generations += 1
        return self.fittest_chromosome()


if __name__ == '__main__':
    length = [10, 42, 100]
    seedList = [15, 42, 30]
    problemNames = []
    list_of_profits = []
    list_of_generations = []
    list_of_times = []
    list_of_knapsack_sizes = []
    generateKnapsackProblemData(length, seedList, problemNames)

    for problem in problemNames:
        population_size = 100

        knapsack_size, item_count, profits, weights = read_from_file(problem)
        weights = np.array(list(weights))
        profits = np.array(list(profits))

        # print(f'Knapsack Size: {knapsack_size}')
        # print('Weight\tProfit')
        # for weight, profit in zip(weights, profits):
        #    print(f'{weight}\t{profit}')

        ga = GeneticAlgorithm(weights=weights,
                              profits=profits,
                              knapsack_size=knapsack_size,
                              population_size=population_size)

        num_of_generations = 100

        start_time = time.process_time()
        solution = ga.evolve(num_of_generations)
        elapsed_time = time.process_time() - start_time

        list_of_profits.append(ga.max_profit)
        list_of_generations.append([*range(1, num_of_generations+1)])
        list_of_times.append(elapsed_time)
        list_of_knapsack_sizes.append(knapsack_size)

    # Pokaż wyniki na wykresach
    plt.figure(figsize=(10, 6))
    # plt.subplot(2, 1, 1)
    plt.plot(list_of_generations[0], list_of_profits[0],
             marker='o', linestyle='-', color='b',
             label=f'Population:100, Elements:{length[0]}')
    plt.plot(list_of_generations[1], list_of_profits[1],
             marker='o', linestyle='-', color='r',
             label=f'Population:100, Elements:{length[1]}')
    plt.plot(list_of_generations[2], list_of_profits[2],
             marker='o', linestyle='-', color='g',
             label=f'Population:100, Elements:{length[2]}')
    plt.xlabel('Number of generation')
    plt.ylabel('Fitness function [1/1]')
    plt.legend()
    plt.title('Change of fitness value on next generations')

    # plt.subplot(2, 1, 2)
    # plt.plot(numberOfTasks, elapsed_time_values,
    #         marker='o', linestyle='-', color='r')
    # plt.xlabel('Run')
    # plt.ylabel('Elapsed Time (s)')
    # plt.title('Elapsed Time vs Run')

    # plt.tight_layout()
    plt.show()
    # print('\nSolution Found')
    # print('Weight\tProfit\tSelect')
    # for weight, profit, gene in zip(weights, profits, solution.genes):
    #    print(f'{weight}\t{profit}\t{gene}')
    # print(f'Max Profit: {solution.fitness}')
