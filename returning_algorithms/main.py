import utils
import getter
import algos

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
                print(algos.robert_flores_ms(matrix))
            elif algo == "rl":
                consequent_list = utils.build_consequent_list(dim[0], arcs)
                print(algos.robert_flores_ln(consequent_list, dim[0]))

            elif algo == "fm":
                matrix = utils.build_adjacency_matrix(dim[0], arcs)
                print(algos.fury_ms(matrix))
            elif algo == "fl":
                consequent_list = utils.build_consequent_list(dim[0], arcs)
                print(algos.fury_ln(consequent_list))
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
                print(algos.robert_flores_ms(matrix))
            elif algo == "rl":
                consequent_list = utils.build_consequent_list(dim[0], arcs)
                print(algos.robert_flores_ln(consequent_list, dim[0]))

            elif algo == "fm":
                matrix = utils.build_adjacency_matrix(dim[0], arcs)
                print(algos.fury_ms(matrix))
            elif algo == "fl":
                consequent_list = utils.build_consequent_list(dim[0], arcs)
                print(algos.fury_ln(consequent_list))
            else:
                print("Nie nie, ze mną tak nie")
    else:
        print("Nie ma takiej opcji :c")