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
            print("KM - khan macierz prawdopodobieństwa")
            print("KL - khan lista następników")
            print("TM - tarjan macierz prawdopodobieństwa")
            print("TL - tarjan lista następników")
            algo = input().lower()

            if algo == "km":
                matrix = utils.build_adjacency_matrix(dim[0], arcs)
                print(sorts.kahn_ms(dim[0], matrix))
            elif algo == "kl":
                consequent_list = utils.build_consequent_list(dim[0], arcs)
                print(sorts.kahn_ln(consequent_list))

            elif algo == "tm":
                matrix = utils.build_adjacency_matrix(dim[0], arcs)
                print("Jeżeli chcesz zacząć od konkretnego wierzchołka podaj od jakiego, jeśli nie wpisz Q")
                vertex = input()

                if(vertex.lower() == "q"):
                    print(sorts.tarjan_ms(dim[0], matrix))

                elif(vertex.isdigit()):
                    print(sorts.tarjan_ms(dim[0], matrix, int(vertex)))
                else:
                    print("Nu nu nu nu")

            elif algo == "tl":
                consequent_list = utils.build_consequent_list(dim[0], arcs)
                print("Jeżeli chcesz zacząć od konkretnego wierzchołka podaj od jakiego, jeśli nie wpisz Q")
                vertex = input()
                print(f"vertex {vertex}")
                if(vertex.lower() == "q"):
                    print(sorts.tarjan_ln(consequent_list))
                elif(vertex.isdigit()):
                    print(sorts.tarjan_ln(consequent_list, int(vertex)))
                else:
                    print("Nu nu nu nu")
            else:
                print("Nie nie, ze mną tak nie")
    if(choice.lower() == 'k'):
        print("Podaj ścieżkę do pliku z którego chcesz wczytać dane: ")
        file_path = input()
        dim,  vertices, arcs = getter.get_data(file_path)
        while True:
            print("Wybierz co chcesz zrobić: ")
            print("KM - khan macierz prawdopodobieństwa")
            print("KL - khan lista następników")
            print("TM - tarjan macierz prawdopodobieństwa")
            print("TL - tarjan lista następników")
            algo = input().lower()

            if algo == "km":
                matrix = utils.build_adjacency_matrix(dim[0], arcs)
                print(sorts.kahn_ms(dim[0], matrix))
            elif algo == "kl":
                consequent_list = utils.build_consequent_list(dim[0], arcs)
                print(sorts.kahn_ln(consequent_list))

            elif algo == "tm":
                matrix = utils.build_adjacency_matrix(dim[0], arcs)
                print("Jeżeli chcesz zacząć od konkretnego wierzchołka podaj od jakiego, jeśli nie wpisz Q")
                vertex = input()

                if(vertex.lower() == "q"):
                    print(sorts.tarjan_ms(dim[0], matrix))

                elif(vertex.isdigit()):
                    print(sorts.tarjan_ms(dim[0], matrix, int(vertex)))
                else:
                    print("Nu nu nu nu")

            elif algo == "tl":
                consequent_list = utils.build_consequent_list(dim[0], arcs)
                print("Jeżeli chcesz zacząć od konkretnego wierzchołka podaj od jakiego, jeśli nie wpisz Q")
                vertex = input()
                print(f"vertex {vertex}")
                if(vertex.lower() == "q"):
                    print(sorts.tarjan_ln(consequent_list))
                elif(vertex.isdigit()):
                    print(sorts.tarjan_ln(consequent_list, int(vertex)))
                else:
                    print("Nu nu nu nu")
            else:
                print("Nie nie, ze mną tak nie")
    else:
        print("Nie ma takiej opcji :c")