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


def new_test():
    algorithms = [knapsack_algos.knapsack_dynamic, knapsack_algos.knapsack_greedy, knapsack_algos.brute_force_knapsack]

    # Test varying number of items for a fixed capacity
    fixed_capacity = 1000
    max_items = 100
    for algo in algorithms:
        print(f"Testing {algo.__name__} with varying number of items (fixed capacity {fixed_capacity}):")
        time_matrix = test_knapsack_vary_items(max_items, fixed_capacity, algo)
        print_matrix(time_matrix)

    # Test varying capacities for a fixed number of items
    fixed_items = 50
    max_capacity = 1000
    for algo in algorithms:
        print(f"Testing {algo.__name__} with varying capacities (fixed items {fixed_items}):")
        time_matrix = test_knapsack_vary_capacity(fixed_items, max_capacity, algo)
        print_matrix(time_matrix)

#test()
new_test()
# max_items = 10
# max_capacity = 10

# result_matrix = test_knapsack(max_items, max_capacity, knapsack_algos.knapsack_dynamic)
# print_matrix(result_matrix)