from logic_solver import *


from queue import LifoQueue


# Function for getting the parsed as a string
def parsed_str(parsed: tuple[str | tuple]) -> str:
    parsed = list(parsed)
    for i in range(len(parsed)):
        if isinstance(parsed[i], tuple):
            if len(parsed[i]) > 1:
                parsed[i] = "(" + parsed_str(parsed[i]) + ")"
            else:
                parsed[i] = parsed_str(parsed[i])
    return SEPARATOR.join(parsed)


# This function parses a mathematical expression represented as a string into a nested tuple structure
# It returns a tuple representing the parsed expression
def parser(text: str) -> tuple[str | tuple]:
    return __remove_brackets(__parse_elems(text))


# This function parses the elements of the expression recursively
# It returns a tuple representing the parsed elements
def __parse_elems(text: str) -> tuple[str | tuple]:
    splitted_text = __split_expr(text.strip())  # Splits the text into individual elements
    selected_op = __select_operator(splitted_text)  # Determine the selected operator

    # Parses the data considering the operation selected (recursively)
    if selected_op:
        index = splitted_text.index(selected_op.__str__())
        if OPERATOR_MAPPING[selected_op] == BI_OP:  # Binary operator
            a = __parse_elems(SEPARATOR.join(splitted_text[:index]))
            b = __parse_elems(SEPARATOR.join(splitted_text[index + 1:]))
            return (a, selected_op, b)
        elif OPERATOR_MAPPING[selected_op] == MONO_OP:  # Unary operator
            a = __parse_elems(SEPARATOR.join(splitted_text[index + 1]))
            return (selected_op, a)

    return (SEPARATOR.join(splitted_text), )  # Return the parsed elements


# This function splits the expression into individual elements
# It returns a list of elements
def __split_expr(text: str) -> tuple[str]:
    # Verify if the number of opening and closing brackets match
    if text.count("(") != text.count(")"):
        raise ValueError("Invalid expression passed.")
    
    text = __remove_brackets(text)  # Remove outer brackets if present

    splitted = []  # List for elements of the expression

    brackets_stack = LifoQueue()  # Stack to keep track of brackets
    buffer = ""  # Buffer for letters between brackets
    for c in text:  # Separate elements according to brackets
        if c == SEPARATOR and brackets_stack.empty():
            splitted.append(buffer)
            buffer = ""
        else:
            if c == "(":
                brackets_stack.put(c)
            elif c == ")":
                brackets_stack.get()
            buffer += c
    splitted.append(buffer)

    return tuple(splitted)


# This function removes outer brackets from the expression
# It returns the modified text
def __remove_brackets(text: str) -> str:
    if text[0] == "(" and text[-1] == ")":  # Remove brackets if they exist
        return text[1:-1]
    else:
        return text


# This function selects the operator with the highest precedence
# It returns the selected operator
def __select_operator(splitted_text: tuple[str]) -> str:
    expr = None  # Default case when no expression is found

    # Decide the operation based on precedence rules
    for operator in OPERATOR_MAPPING:
        if operator in splitted_text:
            expr = operator
            break

    return expr
