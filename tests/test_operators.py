"""
Tests unitaires pour operators.py.

Ce module contient des tests pytest vérifiant le comportement attendu des
fonctions add, subtract, multiply et divide. Chaque fonction de test possède
une docstring décrivant le scénario testé, les entrées et le résultat attendu.
Exécuter depuis la racine du projet pour que l'import de operators fonctionne.
"""
import pytest
from operators import add, subtract, multiply, divide

def test_add():
    """
    Teste l'addition de deux nombres.

    Scénarios:
    - entiers positifs (1 + 2 -> 3)
    - addition avec zéro (1 + 0 -> 1, 0 + 1 -> 1)
    - addition de floats (1.5 + 2.25 -> 3.75)

    Résultat attendu:
    - la fonction renvoie la somme arithmétique a + b.
    """
    assert add(1, 2) == 3
    assert add(1, 0) == 1
    assert add(0, 1) == 1
    assert add(1.5, 2.25) == pytest.approx(3.75)

def test_subtract():
    """
    Teste la soustraction classique a - b.

    Scénarios:
    - subtract(2, 4) -> -2
    - subtract(5, 2) -> 3
    - cas avec zéro (0,1) et (1,0)

    Résultat attendu:
    - la fonction effectue a - b; si le comportement actuel diffère,
      ce test échouera et indiquera un bug d'implémentation.
    """
    assert subtract(2, 4) == -2
    assert subtract(5, 2) == 3
    assert subtract(0, 1) == -1
    assert subtract(1, 0) == 1

def test_multiply():
    """
    Teste la multiplication a * b.

    Scénarios:
    - produit de petits entiers (2*3 -> 6)
    - multiplication par zéro (3*0 -> 0)
    - identités multiplicatives (3*1 -> 3, 1*3 -> 3)

    Résultat attendu:
    - la fonction renvoie le produit arithmétique a * b.
    """
    assert multiply(2, 3) == 6
    assert multiply(3, 0) == 0
    assert multiply(3, 1) == 3
    assert multiply(1, 3) == 3

def test_divide():
    """
    Teste la division réelle a / b.

    Scénarios:
    - division exacte (8/2 -> 4)
    - division d'un zéro en numérateur (0/2 -> 0)
    - division par 1 (2/1 -> 2)
    - division produisant float (7/2 -> 3.5)
    - division par négatif (9/-2 -> -4.5)

    Résultat attendu:
    - la fonction renvoie la division réelle (float) a / b.
    - si l'implémentation actuelle utilise //, ce test échouera.
    """
    assert divide(8, 2) == 4
    assert divide(0, 2) == 0
    assert divide(2, 1) == 2
    assert divide(7, 2) == pytest.approx(3.5)
    assert divide(9, -2) == pytest.approx(-4.5)

def test_divide_by_zero_raises():
    """
    Vérifie que la division par zéro lève une exception ZeroDivisionError.

    Scénario:
    - divide(1, 0) doit lever ZeroDivisionError.

    Résultat attendu:
    - ZeroDivisionError est levée.
    """
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
