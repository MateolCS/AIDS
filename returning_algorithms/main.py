import utils
import getter
import sorts

while True:
    print("Podaj czy chcesz działać na grafie wczytanym z pliku, czy z klawiatury: ")
    print("P - z pliku")
    print("K - klawiatura")
    choice = input()
    if(choice.lower() == 'p'):
        print("Podaj ścieżkę do pliku z którego chcesz wczytać dane: ")
        file_path = input()
        dim,  vertices, arcs = getter.read_data(file_path)
        while True:
            print("Wybierz co chcesz zrobić: ")
            print("RM - robert flores macierz sąsiedztwa")
            print("RL - robert flores lista następników")
            print("FM - fury macierz sąsiedztwa")
            print("FL -  fury lista nas†ępników")
            algo = input().lower()

            if algo == "rm":
                matrix = utils.build_adjacency_matrix(dim[0], arcs)
                print(sorts.kahn_ms(dim[0], matrix))
            elif algo == "rl":
                consequent_list = utils.build_consequent_list(dim[0], arcs)
                print(sorts.kahn_ln(consequent_list))

            elif algo == "fm":
                matrix = utils.build_adjacency_matrix(dim[0], arcs)

            elif algo == "fl":
                consequent_list = utils.build_consequent_list(dim[0], arcs)
                
            else:
                print("Nie nie, ze mną tak nie")
    if(choice.lower() == 'k'):
        dim,  vertices, arcs = getter.get_data()
        while True:
            print("Wybierz co chcesz zrobić: ")
            print("RM - robert flores macierz sąsiedztwa")
            print("RL - robert flores lista następników")
            print("FM - fury macierz sąsiedztwa")
            print("FL -  fury lista nas†ępników")
            algo = input().lower()

            if algo == "rm":
                matrix = utils.build_adjacency_matrix(dim[0], arcs)
                print(sorts.kahn_ms(dim[0], matrix))
            elif algo == "rl":
                consequent_list = utils.build_consequent_list(dim[0], arcs)
                print(sorts.kahn_ln(consequent_list))

            elif algo == "fm":
                matrix = utils.build_adjacency_matrix(dim[0], arcs)

            elif algo == "fl":
                consequent_list = utils.build_consequent_list(dim[0], arcs)
                
            else:
                print("Nie nie, ze mną tak nie")
    else:
        print("Nie ma takiej opcji :c")