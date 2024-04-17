import math
import sympy as sp

def fourier_series(signal, t):
    return sp.fourier_series(signal, (t, -sp.pi, sp.pi))

def calculate_attenuation(signal, distance, environment):
    if environment == 'guided':
        k = 0.5  # replace with actual value
        attenuation = 10 ** (k * distance)
    else:  # unguided
        n = 2  # replace with actual value
        attenuation = distance ** (-n)
    return attenuation

def convert_to_db(attenuation, initial_power):
    traveled_signal_power = initial_power * attenuation
    return 10 * math.log10(traveled_signal_power / initial_power)

# User input
signal = input("Enter the digital signal: ")
distance = float(input("Enter the distance traveled: "))
environment = input("Enter the environment (guided/unguided): ")

# Calculate attenuation
t = sp.symbols('t')
signal = fourier_series(signal, t)
attenuation = calculate_attenuation(signal, distance, environment)

# Convert to dB
initial_power = 1  # replace with actual value
db = convert_to_db(attenuation, initial_power)

print(f"The signal attenuation is {db} dB.")