"""
Escribe un programa en Python llamado bisiestos.py que cree una función llamada
numbisiestos() a la que se le pasan dos años. La función tendrá que calcular el número de años
bisiestos que hay entre esos dos años (incluyendo los dos años) y el número de días total entre
esos dos años (incluyendo los dos años). El programa pedirá al usuario que introduzca los dos
años y mostrará en la consola el resultado de la comprobación.
Crea una función llamada es_bisiesto() que calcule si un año es bisiesto o no sabiendo que los
años bisiestos son múltiplos de 4. Si un año es divisible entre 4 pero no entre 100, entonces SÍ es
un año bisiesto. Si un año es divisible entre 100 y 400, entonces SÍ es un año bisiesto. Si un año es
divisible entre 100 pero no entre 400, entonces NO es un año bisiesto. En otros casos, tampoco.
"""


def isYearLeap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def numLeap(year1, year2):
    total_YearLeap = 0
    total_days = 0
    for year in range(year1, year2 + 1):
        total_days += 365
        if isYearLeap(year):
            total_YearLeap += 1
            total_days += 1
    print("Entre los años", year1, "y", year2, "hay", total_YearLeap, "años bisiestos y un total de", total_days,
          "días.")


y1 = int(input("Introduce el primer año: "))
y2 = int(input("Introduce el segundo año: "))

numLeap(y1, y2)
