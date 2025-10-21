# Module static/

## Raison d'être du module

Fournir les ressources statiques (CSS) de la calculatrice Flask :

- Apparence visuelle et mise en page de l'interface
- Thème sombre avec distinction visuelle des opérateurs
- États interactifs pour feedback utilisateur
- Layout responsive centré

## Structure du module

```
static/
├── style.css          # Feuille de style principale
└── README.md          # Documentation du module (ce fichier)
```

## Principaux fichiers & responsabilités

### static/style.css

**Responsabilités :**

- Définition du thème visuel (couleurs, typographie, espacements)
- Mise en page avec Flexbox (centrage) et CSS Grid (grille de boutons 4×4)
- États interactifs des boutons (hover, active)
- Style différencié pour les opérateurs (classe `.operator`)
- Style du champ d'affichage (#display) en lecture seule

**Sélecteurs principaux :**

- `body` : Centrage général et background de la page
- `.calculator` : Conteneur principal (max-width 600px, background sombre)
- `#display` : Champ d'affichage des résultats (texte aligné à droite)
- `.buttons` : Grille CSS 4 colonnes avec gap de 15px
- `.btn` : Style de base pour tous les boutons
- `.operator` : Surcharge pour les boutons d'opération (orange)

## Dépendances & hypothèses

### Dépendances

- **HTML** : Nécessite les classes `.calculator`, `.buttons`, `.btn`, `.operator` et l'ID `#display` dans templates/index.html
- **Flask** : Doit servir ce fichier via la route `/static/style.css`
- **Navigateurs** : Requiert support CSS Grid et Flexbox (IE11+)

### Hypothèses

- **Structure HTML stable** : Le CSS suppose une hiérarchie fixe des éléments
- **Grille 4 colonnes** : Conçu pour 16 boutons (4×4), nombre de boutons doit être multiple de 4
- **Pas de media queries** : Design responsive via max-width uniquement, pas d'adaptation mobile
- **Thème unique** : Uniquement mode sombre, pas de variables CSS pour changements de thème
- **Police système** : Utilise Arial (disponible partout), pas de fonts externes
- **Valeurs fixes** : max-width 600px, grid 4 colonnes, gap 15px, display 36px

### Limitations connues

- Pas de responsive pour mobile/tablette (grille reste 4 colonnes)
- Pas de mode clair disponible
- Absence de states `focus` pour accessibilité clavier
- Couleurs hardcodées (maintenance difficile pour changements de thème)

## Fichiers liés

- **templates/index.html** : Référence ce fichier via `{{ url_for('static', filename='style.css') }}`
- **app.py** : Configure le dossier static et sert ces fichiers
