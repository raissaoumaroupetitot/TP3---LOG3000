# Tests

Ce répertoire contient la suite de tests pytest pour le projet Calculatrice Web.

## But

Valider la logique des opérations (operators.py)

## Prérequis

- Python 3.8+
- pytest

## Installation

```bash
pip install -r ../requirements.txt
```

## Run des tests

```bash
pytest -q
```

## Couverture des tests

### test_operators.py

| Test | Fonction testée | Scénarios couverts |
|------|----------------|-------------------|
| `test_add()` | `add(a, b)` | Entiers positifs, zéro, floats |
| `test_subtract()` | `subtract(a, b)` | Résultats positifs/négatifs, zéro |
| `test_multiply()` | `multiply(a, b)` | Produit, multiplication par 0 et 1 |
| `test_divide()` | `divide(a, b)` | Division exacte, floats, nombres négatifs |
| `test_divide_by_zero_raises()` | `divide(a, b)` | Exception ZeroDivisionError |

## Détails importants

- **test_divide()** : Vérifie que la division utilise `/` (division réelle) et non `//` (division entière)
- Tous les tests incluent des cas limites (zéro, négatifs, floats)

## Interprétation

- **Tests réussis** : Toutes les opérations fonctionnent correctement
- **Tests échoués** : Un bug existe dans `operators.py` - vérifier l'implémentation
