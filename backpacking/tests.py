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


def test():
    for i in range(1000, 10000, 1000):
        sizes, values, capacity = generate_knapsack_problem(i)
        print("Dynamic Knapsack: \n")
        test_algo(knapsack_algos.knapsack_dynamic, sizes, values, capacity, i)
        print("Greedy Knapsack: \n")
        test_algo(knapsack_algos.knapsack_greedy, sizes, values, capacity, i)
        print("Brootforce Knapsack: \n")
        test_algo(knapsack_algos.brute_force_knapsack, sizes, values, capacity, i)


test()