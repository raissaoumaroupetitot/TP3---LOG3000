## Raison d'être du module

Fournir l'interface utilisateur de la calculatrice Flask :

- Affichage du résultat de calcul ({{ result }})
- Saisie d'expressions via boutons numériques et opérateurs
- Envoi de l'expression en POST au serveur
- Réaffichage du résultat dans la même page

## Structure du module

templates/
├── index.html # Interface principale (ce fichier)
└── README.md # Documentation du module templates

## Principaux fichiers & responsabilités

### templates/index.html

**Responsabilités principales :**

- Structure HTML de la calculatrice (.calculator, #display, .buttons)
- Formulaire method="POST" qui envoie le champ `display` à `/`
- JavaScript embarqué :
  - `appendToDisplay(value)` : Concatène la saisie dans #display
  - `clearDisplay()` : Réinitialise l'affichage
- Référence CSS : {{ url_for('static', filename='style.css') }}

## Dépendances & hypothèses

### Dépendances

- Flask/Jinja2 pour le rendu de {{ result }} et url_for()
- static/style.css pour la mise en forme (grille 4 colonnes, thème sombre)
- Backend Flask avec route `/` acceptant GET et POST

### Hypothèses

- **Calcul serveur uniquement** : Aucune évaluation côté client
- **Champ readonly** : #display est en lecture seule, saisie via boutons uniquement
- **Une opération par soumission** : Le backend traite une seule expression binaire
- **Gestion des erreurs** : Le backend renvoie "Error" dans result en cas d'échec
- **Valeur initiale** : {{ result }} est vide ("") ou None au premier chargement (GET)
