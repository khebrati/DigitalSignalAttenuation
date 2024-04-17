import math
import sympy as sp
from sympy import symbols,sin,cos,sympify

def convert_to_db(signla_in_w):
    return 10 * math.log10(signla_in_w)

# User input
signal_string = input("Enter the digital signal: ")
# distance = float(input("Enter the distance traveled: "))
# environment = input("Enter the environment (guided/unguided): ")

t = symbols('t')
signal = sympify(signal_string)
signal_terms = signal.as_ordered_terms()
for term in signal_terms:
    print(term)
# sin_cos_functions = [terms.args[0] for term in terms]