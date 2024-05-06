#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1 # Décrémenter n à chaque itération
    return result


if len(sys.argv) != 2:
    print("Usage: python script.py <number>")
    sys.exit(1)

try:
    number = int(sys.argv[1])
except ValueError:
    print("Erreur : L'argument doit être un nombre entier.")
    sys.exit(1)

if number < 0:
    print("Erreur : Le nombre doit être positif.")
    sys.exit(1)

f = factorial(number)
print(f)
