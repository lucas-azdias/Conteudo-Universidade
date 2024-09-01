from logic_solver import *


from tabulate import tabulate
from typing import Iterable


class truth_table:

    def __init__(self, exprs: Iterable[str] = None) -> None:
        self.__exprs = list()  # List of expressions -> ("expression passed", "expression parsed", "variables found in the expression parsed")
        
        if exprs:  # Adds all expressions passed if any
            self.extend(exprs)
    

    def __str__(self) -> str:
        if len(self.__exprs) > 0:
            return tabulate(self.build_table(), headers="firstrow")
        else:
            return "<Empty truth table>"
    

    def append(self, expr: str) -> None:
        # Adds the expression passed
        if not self.has_expr(expr):
            parsed = tools.parser(expr)  # Parses the expression
            self.__exprs.append((expr, parsed, truth_table.find_vars(parsed)))
    

    def insert(self, index: int, expr: str) -> None:
        # Adds the expression in the index passed
        if not self.has_expr(expr):
            parsed = tools.parser(expr)  # Parses the expression
            self.__exprs.insert(index, (expr, parsed, truth_table.find_vars(parsed)))
    

    def extend(self, exprs: Iterable[str]) -> None:
        # Adds all expressions passed
        for expr in exprs:
            self.append(expr)
    

    def pop(self, index: int) -> None:
        # Removes the expression in the index passed
        self.__exprs.pop(index)
    

    def remove(self, expr: str) -> None:
        # Removes the expression passed
        for i, (cur_expr, _, _) in self.__exprs:
            if cur_expr == expr:
                self.pop(i)
                break
    

    def has_expr(self, expr: str) -> bool:
        # Returns if the expression has already been put
        return any((cur_expr == expr) or (tools.parsed_str(cur_parsed) == tools.parsed_str(tools.parser(expr))) for cur_expr, cur_parsed, _ in self.__exprs)
    

    def vars(self) -> tuple[str]:
        # Builds a tuple with all variables found in the expressions list
        vars = list()
        for _, _, cur_vars in self.__exprs:
            vars.extend(cur_vars)
        return tuple(sorted(set(vars)))


    def exprs(self) -> tuple[str]:
        # Returns all expressions
        return tuple([expr for expr, _, _ in self.__exprs])
    

    def build_table(self) -> tuple[tuple[str]]:
        # Builds the vars table structure and puts all variable values in the table
        vars_table = truth_table.build_vars_table(self.vars())

        # Creates the truth table
        table = list(vars_table)

        for _, parsed, _ in self.__exprs:
            # Puts in the table another column with the result of the parsed expression considering the variables values
            table.append(truth_table.build_parsed_column(parsed, vars_table))
        
        # Transpose the table
        table = tuple(zip(*table))

        return table
    

    def display(self):
        print(self.__str__())

    
    @staticmethod
    def find_vars(parsed: tuple[str | tuple]) -> tuple[str]:
        # Finds all variables based on the amount of values in the tuple
        vars = []

        if len(parsed) == 1:
            vars.append(parsed[0])
        else:
            for elem in parsed:
                if isinstance(elem, tuple):
                    vars.extend(truth_table.find_vars(elem))
        
        return tuple(vars)
    

    @staticmethod
    def build_vars_table(vars: tuple[str]) -> tuple[tuple[str]]:
        # Builds the table structure and puts all variable values in the table
        table = [[None for _ in range(pow(2, len(vars)) + 1)] for _ in range(len(vars))]

        current_value = False  # Current value to be placed in the table
        for i in range(len(table)):
            flip_num = pow(2, len(table) - i - 1)  # Checks when to flip the value being put in the table
            table[i][0] = vars[i]  # Header for the variable values
            for j in range(1, len(table[i])):
                if (j - 1) % flip_num == 0:  # Flips value
                    current_value = not current_value
                table[i][j] = TRUE if current_value else FALSE  # Places the value
            table[i] = tuple(table[i])

        return tuple(table)
    

    @staticmethod
    def build_parsed_column(parsed: tuple[str | tuple], vars_table: tuple[tuple[str]]) -> tuple[str]:
        # Returns a new column to be add in the table with the result of the parsed expression considering the variables values
        parsed_col = []

        # Calculates the values for the new column
        for i in range(len(vars_table[0]) - 1):
            cur_vars_values = {var_column[0]: var_column[i + 1] for var_column in vars_table}
            parsed_col.append(truth_table.calculate_value(parsed, cur_vars_values))

        # Puts the header for the new column
        parsed_col.insert(0, tools.parsed_str(parsed))

        return tuple(parsed_col)


    @staticmethod
    def calculate_value(parsed: tuple[str | tuple], vars_values: dict[str, str]) -> bool:
        # Calculates the logical value of the expression (recursively)
        if len(parsed) == 3:  # Binary operator
            a = truth_table.calculate_value(parsed[0], vars_values)
            op = parsed[1]
            b = truth_table.calculate_value(parsed[2], vars_values)

            if op == BI_IMPLICATION:
                return expr_solvers.biimplication_solver(a, b)
            elif op == IMPLICATION:
                return expr_solvers.implication_solver(a, b)
            elif op == DISJUNCTION:
                return expr_solvers.disjunction_solver(a, b)
            elif op == CONJUNCTION:
                return expr_solvers.conjunction_solver(a, b)
            else:
                raise ValueError("Invalid operator found")

        elif len(parsed) == 2:  # Unary operator
            op = parsed[0]
            a = truth_table.calculate_value(parsed[1], vars_values)

            if op == NEGATION:
                return expr_solvers.negation_solver(a)
            else:
                raise ValueError("Invalid operator found")

        elif len(parsed) == 1:  # Variable found (stop condition)
            return vars_values[parsed[0]]

        else:  # Error
            raise ValueError("Invalid expression passed")
