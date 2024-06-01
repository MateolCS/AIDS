import random
import knapsack_algos
from timeit import default_timer as timer
import sys
sys.setrecursionlimit(500000000)

def test_algo(algorithm, weights, values, capacity, n):
    start_time = timer()
    algorithm(capacity, weights, values, n)
    end_time = timer()
    print(f"Number of elements: {n}, capacity: {capacity}, time: {end_time-start_time}")


def generate_knapsack_problem(n):
    # Generowanie listy rozmiarów i wartości
    sizes = [random.randint(1, 100) for _ in range(n)]  # losowy rozmiar w przedziale od 1 do 100
    values = [random.randint(1, 1000) for _ in range(n)]  # losowa wartość w przedziale od 1 do 1000
    
    # Ustalenie pojemności plecaka jako pewna proporcja sumy rozmiarów
    total_size = sum(sizes)
    capacity = random.randint(1, total_size // 2)  # pojemność w przedziale od 1 do połowy sumy rozmiarów
    
    return sizes, values, capacity


def test_knapsack_vary_items(max_items, capacity, algo):
    time_matrix = [0 for _ in range(max_items + 1)]

    for num_items in range(1, max_items + 1):
        values = [random.randint(1, 100) for _ in range(num_items)]
        weights = [random.randint(1, 100) for _ in range(num_items)]

        start_time = timer()
        algo(capacity, weights, values, num_items)
        end_time = timer()
        execution_time = end_time - start_time
        time_matrix[num_items] = execution_time
    
    return time_matrix

def test_knapsack_vary_capacity(num_items, max_capacity, algo):
    time_matrix = [0 for _ in range(max_capacity + 1)]

    values = [random.randint(1, 100) for _ in range(num_items)]
    weights = [random.randint(1, 100) for _ in range(num_items)]

    for capacity in range(1, max_capacity + 1):
        start_time = timer()
        algo(capacity, weights, values, num_items)
        end_time = timer()
        execution_time = end_time - start_time
        time_matrix[capacity] = execution_time
    
    return time_matrix

def test_knapsack(max_items, max_capacity, algo):

    time_matrix = [[0 for _ in range(max_capacity + 1)] for _ in range(max_items + 1)]

    for num_items in range(1, max_items + 1):
        values = [random.randint(1, 100) for _ in range(num_items)]
        weights = [random.randint(1, 100) for _ in range(num_items)]

        for capacity in range(1, max_capacity + 1):
            start_time = timer()
            algo(capacity, weights, values, num_items)
            end_time = timer()
            execution_time = end_time - start_time
            time_matrix[num_items][capacity] = execution_time
    
    return time_matrix

def print_matrix(matrix):
    if isinstance(matrix[0], list):  
        for row in matrix:
            print("\t".join(map(str, row)))
    else:  
        print("\t".join(map(str, matrix)))



def test():
    for i in range(1000, 10000, 1000):
        sizes, values, capacity = generate_knapsack_problem(i)
        print("Dynamic Knapsack: \n")
        test_algo(knapsack_algos.knapsack_dynamic, sizes, values, capacity, i)
        print("Greedy Knapsack: \n")
        test_algo(knapsack_algos.knapsack_greedy, sizes, values, capacity, i)
        print("Brootforce Knapsack: \n")
        test_algo(knapsack_algos.brute_force_knapsack, sizes, values, capacity, i)

def test_knapsack_fixed_capacity(fixed_capacity, min_items, max_items, step, algo):
    execution_times = []

    for num_items in range(min_items, max_items + 1, step):
        values = [random.randint(1, 100) for _ in range(num_items)]
        weights = [random.randint(1, 100) for _ in range(num_items)]

        start_time = timer()
        algo(fixed_capacity, weights, values, num_items)
        end_time = timer()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
    
    return execution_times



def test_knapsack_fixed_items(num_items, min_capacity, max_capacity, step, algo):
    execution_times = []

    values = [random.randint(1, 100) for _ in range(num_items)]
    weights = [random.randint(1, 100) for _ in range(num_items)]

    for capacity in range(min_capacity, max_capacity + 1, step):
        start_time = timer()
        algo(capacity, weights, values, num_items)
        end_time = timer()
        execution_time = end_time - start_time
        execution_times.append(execution_time)
    
    return execution_times


def test_knapsack_matrix(min_items, max_items, item_step, min_capacity, max_capacity, capacity_step, algo):
    num_rows = (max_capacity - min_capacity) // capacity_step + 1
    num_cols = (max_items - min_items) // item_step + 1

    time_matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    for i, capacity in enumerate(range(min_capacity, max_capacity + 1, capacity_step)):
        for j, num_items in enumerate(range(min_items, max_items + 1, item_step)):
            values = [random.randint(1, 100) for _ in range(num_items)]
            weights = [random.randint(1, 100) for _ in range(num_items)]

            start_time = timer()
            algo(capacity, weights, values, num_items)
            end_time = timer()
            execution_time = end_time - start_time
            time_matrix[i][j] = execution_time
    
    return time_matrix


def fixed_capacity():
    fixed_capacity = 10
    min_items = 100
    max_items = 1000
    step = 100

    algorithms = [knapsack_algos.knapsack_dynamic, knapsack_algos.knapsack_dynamic, knapsack_algos.brute_force_knapsack]

    for algo in algorithms:
        print(f"Testing {algo.__name__} with fixed capacity {fixed_capacity} and varying number of items:")
        execution_times = test_knapsack_fixed_capacity(fixed_capacity, min_items, max_items, step, algo)
        print(f"Execution times for {algo.__name__}: {execution_times}")


def fixed_items():
    fixed_items = 100
    min_capacity = 100
    max_capacity = 1000
    step = 100

    algorithms = [knapsack_algos.knapsack_dynamic, knapsack_algos.knapsack_dynamic, knapsack_algos.brute_force_knapsack]

    for algo in algorithms:
        print(f"Testing {algo.__name__} with fixed number of items {fixed_items} and varying capacities:")
        execution_times = test_knapsack_fixed_items(fixed_items, min_capacity, max_capacity, step, algo)
        print(f"Execution times for {algo.__name__}: {execution_times}")

def matrix_test():
    min_items = 10
    max_items = 100
    item_step = 10
    min_capacity = 10
    max_capacity = 100
    capacity_step = 10

    algorithms = [knapsack_algos.knapsack_dynamic, knapsack_algos.knapsack_dynamic, knapsack_algos.brute_force_knapsack]

    for algo in algorithms:
        print(f"Testing {algo.__name__} with increasing capacities and number of items:")
        time_matrix = test_knapsack_matrix(min_items, max_items, item_step, min_capacity, max_capacity, capacity_step, algo)
        print_matrix(time_matrix)

#test()
fixed_capacity()
print("\n\n")
fixed_items()
print("\n\n")
matrix_test()
# max_items = 10
# max_capacity = 10

# result_matrix = test_knapsack(max_items, max_capacity, knapsack_algos.knapsack_dynamic)
# print_matrix(result_matrix)