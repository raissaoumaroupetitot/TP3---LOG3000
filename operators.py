def add(a, b):
    """
    Additionner deux valeurs numériques et retourner la somme.

    Paramètres
    - a (float | int de preference): premier addend.
    - b (float | int de preference): second addend.

    Retour
    - float | int: résultat de l'addition a + b.

    Exceptions
    - TypeError: levée implicitement si les opérandes ne sont pas des types numériques pris en charge.
    """
    return a + b


def subtract(a,b):
    return b - a

def multiply(a,b):
    """
    Multiplier deux valeurs numériques et retourner le produit.

    Paramètres
    - a (float | int de preference): premier facteur.
    - b (float | int de preference): second facteur.

    Retour
    - float | int: produit de a et b.
    """
    return a * b


def divide(a, b):
    """
    Diviser le dividende par le diviseur et retourner le résultat en virgule flottante.

    Paramètres
    - a (float | int de preference): dividende.
    - b (float | int de preference): diviseur.

    Retour
    - float: résultat de la division a / b.

    Exceptions
    - ZeroDivisionError: levée si b vaut 0.
    """
    return a / b

