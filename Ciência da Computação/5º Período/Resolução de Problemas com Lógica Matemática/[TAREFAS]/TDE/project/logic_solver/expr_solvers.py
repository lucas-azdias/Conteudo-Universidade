from logic_solver import *


def biimplication_solver(a: str, b: str) -> bool:
    a_bool = __convert_value(a)
    b_bool = __convert_value(b)
    return TRUE if ((not a_bool) or b_bool) and ((not b_bool) or a_bool) else FALSE


def implication_solver(a: str, b: str) -> bool:
    a_bool = __convert_value(a)
    b_bool = __convert_value(b)
    return TRUE if (not a_bool) or b_bool else FALSE


def disjunction_solver(a: str, b: str) -> bool:
    a_bool = __convert_value(a)
    b_bool = __convert_value(b)
    return TRUE if a_bool or b_bool else FALSE


def conjunction_solver(a: str, b: str) -> bool:
    a_bool = __convert_value(a)
    b_bool = __convert_value(b)
    return TRUE if a_bool and b_bool else FALSE


def negation_solver(a: str) -> bool:
    a_bool = __convert_value(a)
    return TRUE if not a_bool else FALSE


def __convert_value(a: str) -> bool:
    if a == TRUE:
        return True
    elif a == FALSE:
        return False
    else:
        raise ValueError("Invalid table value found")
