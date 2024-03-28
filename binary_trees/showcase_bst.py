from tree import Tree
from generator import Generator

class Showcase:
    def __init__(self) -> None:
        self.generator = Generator()
        self.begin_showcase()


    def begin_showcase(self):
        n = int(input("Podaj z ilu elementow chcesz zbudować drzewo: "))
        tree = Tree(self.generator.generate(n))
        tree.print_tree()
        
        while True:
            print("Wybierz to co chcesz zrobic: ")
            print("L - znajdź minimum")
            print("H - znajdź maksimum")
            print("P - podanie poziomu i usuniecie wezla")
            print("I - malejace wypisanie")
            print("U - usuwanie poddrzewa")
            print("R - rownowazenie drzewa")
            print("Q - koniec")
            choice = input()
            if choice.upper() == "L":
                print(tree.get_min())
            elif choice.upper() == "H":
                print(tree.get_max())
            elif choice.upper() == "P":
                val = int(input("Podaj wartosc"))
                print(tree.get_all_level_nodes(val))
                tree.print_tree()
            elif choice.upper() == "I":
                print(tree.get_decreasing(tree.root))
            elif choice.upper() == "U":
                val = int(input("Podaj wartosc"))
                tree.find_and_delete(val)
                tree.print_tree()
            elif choice.upper() == "R":
                print(tree.get_preorder(tree.root))
                tree.root = tree.correct_balance(tree.root)
                print(tree.get_preorder(tree.root))
                tree.print_tree()
            elif choice.upper() == "Q":
                return 
            else:
                print("Invalid command\n")


showcase = Showcase()
showcase.begin_showcase()