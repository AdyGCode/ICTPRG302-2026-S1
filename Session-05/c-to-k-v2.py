# Filename: c-to-k-v2.py

def celcius_to_kelvin(temperature):
    # Convert to kelvin
    temperature_kelvin = 273.15 + temperature
    # Return the result
    return temperature_kelvin


def get_decimal_number(prompt):
    number = input(prompt)
    number = float(number)
    return number


celcius = get_decimal_number("What is the temperature (C): ")

kelvin = celcius_to_kelvin(celcius)

print("Temperature: " + str(kelvin) + "K")
