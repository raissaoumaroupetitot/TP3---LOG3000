def add(a,b):
    return a + b

def subtract(a,b):
    """
    Soustraire le second nombre du premier et retourner la différence.
    
    Paramètres
    - a : premier nombre (celui duquel on soustrait).
    - b : second nombre (celui qu'on soustrait).
    
    Retour
    - float | int: différence de a - b.
    """
    return a - b

def multiply(a,b):
    """
    Multiplier deux valeurs numériques et retourner le produit.

    Paramètres
    - a : premier facteur.
    - b : second facteur.

    Retour
    - float | int: produit de a et b.
    """
    return a * b


def divide(a, b):
    """
    Diviser le dividende par le diviseur et retourner le résultat en virgule flottante.

    Paramètres
    - a : dividende.
    - b : diviseur.

    Retour
    - float: résultat de la division a / b.

    Exceptions
    - ZeroDivisionError: levée si b vaut 0.
    """
    return a / b

