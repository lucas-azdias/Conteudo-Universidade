# Separator text for the inputs
SEPARATOR = " "


# Operators texts for the inputs
BI_IMPLICATION = "<->"
IMPLICATION = "->"
DISJUNCTION = "v"
CONJUNCTION = "^"
NEGATION = "~"
# BI_IMPLICATION = r"\leftrightarrow"
# IMPLICATION = r"\rightarrow"
# DISJUNCTION = r"\vee"
# CONJUNCTION = r"\wedge"
# NEGATION = r"\neg"


# Enum for each type of operators
BI_OP = 0
MONO_OP = 1


# Mapping of operators to their types
OPERATOR_MAPPING = {
    BI_IMPLICATION: BI_OP,
    IMPLICATION: BI_OP,
    DISJUNCTION: BI_OP,
    CONJUNCTION: BI_OP,
    NEGATION: MONO_OP
}


# True and False default symbols
TRUE = "T"
FALSE = "F"


from logic_solver import tools
from logic_solver import expr_solvers
from logic_solver import truth_table
