from logic_solver import *


from os import system
from time import sleep


def test_truth_table():
    # Test stage
    my_truth_table = truth_table.truth_table()

    system("cls")

    print("Testing truth table...")
    print()

    exprs = [
        SEPARATOR.join(["A", IMPLICATION, "B", DISJUNCTION, "C"]),
        SEPARATOR.join(["B", DISJUNCTION, "D", BI_IMPLICATION, "A"]),
        SEPARATOR.join(["A", CONJUNCTION, "B", CONJUNCTION, "(C", DISJUNCTION, "B)", IMPLICATION, "D"])
    ]

    my_truth_table.extend(exprs)

    print(my_truth_table)
    print()

    input("<Press any key to continue>")


def interactive_truth_table():
    # User-demand stage
    my_truth_table = truth_table.truth_table()

    # Interactive menu
    while True:
        system("cls")

        # Options
        print("[1] Show the truth table")
        print("[2] Add a new expression to the truth table")
        print("[3] Remove a expression from the truth table")
        print("[0] Exit")

        # Select option
        response = input("> ")
        print()

        # Treat given option
        if response.isnumeric():
            match int(response):
                case 1:  # Show truth table
                    my_truth_table.display()
                    print()
                    input("<Press any key to continue>")
                case 2:  # Add expression
                    print(f"Usable symbols\
                    \nBi-implication: \"{BI_IMPLICATION}\"\
                    \nImplication: \"{IMPLICATION}\"\
                    \nDisjunction: \"{DISJUNCTION}\"\
                    \nConjunction: \"{CONJUNCTION}\"\
                    \nNegation: \"{NEGATION}\"\
                    \nSeparator: \"{SEPARATOR}\"\
                    \n")

                    print("Type your expression:")
                    response = input("> ")
                    if response != "":
                        if not my_truth_table.has_expr(response):
                            my_truth_table.append(response)
                            print("\nExpression added sucessfully.")
                        else:
                            print("\nUnable to add expression.")
                        sleep(0.65)
                case 3:  # Remove expression
                    print("Type the index of your expression:")
                    response = input("> ")
                    if response != "":
                        if response.isnumeric() and len(my_truth_table.exprs()) > int(response) - 1:
                            my_truth_table.pop(int(response) - 1)
                            print("\nExpression removed sucessfully.")
                        else:
                            print("\nUnable to remove expression.")
                        sleep(0.65)
                case 0:  # Exit
                    system("cls")
                    print("Program finished.\n")
                    break
                case _:  # Invalid input
                    continue


if __name__ == "__main__":
    # Test stage
    test_truth_table()

    # User-demand stage
    interactive_truth_table()
