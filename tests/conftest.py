"""
Assure que la racine du projet (parent de tests/) est dans sys.path
afin que les imports relatifs comme `import operators` fonctionnent
lors de l'exécution des tests depuis l'IDE ou CI.
"""
import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
