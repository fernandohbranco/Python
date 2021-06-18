# temperature converter
import sys

def from_kelvin(temp):
    global kelvin, celsius, fahrenheit, rankine
    kelvin = temp
    celsius = temp - 273.15
    fahrenheit = (temp * 9 / 5) - 459.67
    rankine = temp * 9 / 5

def from_celsius(temp):
    global kelvin, celsius, fahrenheit, rankine
    kelvin = temp + 273.15
    celsius = temp
    fahrenheit = (temp * 9 / 5) + 32
    rankine = (temp * 9 / 5) + 491.67

def from_fahrenheit(temp):
    global kelvin, celsius, fahrenheit, rankine
    kelvin = (temp + 459.67) * 5 / 9
    celsius = (temp - 32) * 5 / 9
    fahrenheit = temp
    rankine = temp + 459.67

def from_rankine(temp):
    global kelvin, celsius, fahrenheit, rankine
    kelvin = temp * 5 / 9
    celsius = (temp * 5 / 9) - 273.15
    fahrenheit = temp - 459.67
    rankine = temp


info = [{"name": "Kelvin", "symbol": "K"}, {"name": "Celsius", "symbol": "ºC"},
        {"name": "Fahrenheit", "symbol": "ºF"}, {"name": "Rankine", "symbol": "ºR"}]

try:
    unit = int(input("""Please, inform the unit:
0 to  (K) Kelvin
1 to (ºC) Celsius
2 to (ºF) Fahrenheit
3 to (ºR) Rankine
> """))

    check = 0
    while check == 0:
        print("")
        unit = int(input("Please inform the unit: "))
        if unit in range(0,len(info)):
            check = 1

    temp = float(input(f"What is the temperature in {info[unit]['name']}? > "))

except:
    sys.exit("Error, type just numbers!")

if unit == 0:
    from_kelvin(temp)

elif unit == 1:
    from_celsius(temp)

elif unit == 2:
    from_fahrenheit(temp)

elif unit == 3:
    from_rankine(temp)

print(f"""
Given Temperature: {temp} {info[unit]['symbol']}
> Kelvin:     {round(kelvin, 2)} K
> Celsius:    {round(celsius, 2)} ºC
> Fahrenheit: {round(fahrenheit, 2)} ºF
> Rankine:    {round(rankine, 2)} ºR
""")