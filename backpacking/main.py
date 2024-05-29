import knapsack_algos


def main():

    while True:
        values = list(map(int, input("Podaj wartości").split()))
        weights = list(map(int, input("Podaj wagi").split()))
        capacity = int(input("Podaj pojemnosc"))
        n = len(values)

        print(f"Broot force knapsack: \n")
        print(knapsack_algos.brute_force_knapsack(capacity, weights, values, n))
        print("-----------------------------\n")
        
        print("Knapsack greedy: \n")
        print(knapsack_algos.knapsack_greedy(capacity, weights, values, n))
        print("------------------------------\n")

        print("Knapsack dynamic: \n")
        print(knapsack_algos.knapsack_dynamic(capacity, weights, values, n))
        print("---------------------------------\n")
    


main()