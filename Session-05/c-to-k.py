# Filename: c-to-k.py

def celcius_to_kelvin(temperature):
    # Convert to kelvin
    temperature_kelvin = 273.15 + temperature
    # Return the result
    return temperature_kelvin


celcius = input("What is the temperature (C): ")
celcius = float(celcius)

kelvin = celcius_to_kelvin(celcius)

print("Temperature: "+ str(kelvin) + "K")
