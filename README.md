# Calculatrice Web – Équipe 23

## 🎯 Objectif du projet

Application web de calculatrice développée avec Flask (Python) permettant d'effectuer des opérations arithmétiques de base (addition, soustraction, multiplication, division).

## 👥 Équipe

- **Numéro d'équipe :** 23  
- **Membres :** 
  - Raissa Oumarou Petitot
  - Joey Hasrouny
  - Gabriel Mejia

## 📋 Fonctionnalités

- Addition de deux nombres
- Soustraction de deux nombres
- Multiplication de deux nombres (a*b)
- Division entière de deux nombres (a//b)
- Interface web intuitive

## 🔧 Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python 3.8+**
- **pip** (gestionnaire de paquets Python)
- **Git** (pour cloner le dépôt)

## 🚀 Installation et configuration

### 1. Cloner le dépôt
```bash
git clone https://github.com/raissaoumaroupetitot/TP3---LOG3000.git
cd TP3---LOG3000
```

### 2. Créer un environnement virtuel (recommandé)

**Sur Linux/Mac :**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Sur Windows :**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer l'application
```bash
python app.py
```

Vous devriez voir un message similaire à :
```
 * Running on http://127.0.0.1:5000
```

### 5. Accéder à l'application

Ouvrez votre navigateur web et accédez à :
```
http://127.0.0.1:5000
```

## 📖 Utilisation

1. Entrez la premiere operande avec les boutons des chiffres
2. Sélectionnez l'opération souhaitée (addition, soustraction, multiplication, division)
3. Entrez la seonde operande avec les boutons des chiffres
4. Cliquez sur le bouton "Calculer"
5. Le résultat s'affichera à l'écran

## 🧪 Tests

Les tests unitaires sont situés dans le dossier `tests/`.

### Exécuter les tests
```bash
pytest tests/
```

Ou avec coverage :
```bash
pytest --cov=. tests/
```

## 🌿 Flux de contribution

### Structure des branches

- **`main`** : branche principale (code stable et testé)
- **`bugfix/[nom]`** : corrections de bugs
  - `bugfix/divide` : correction du bug de division
  - `bugfix/multiply` : correction du bug de multiplication
  - `bugfix/substract` : correction du bug de soustraction

### Processus de contribution

1. **Créer une branche** depuis `main` :
```bash
git checkout main
git pull origin main
git checkout -b bugfix/nom-du-bug
```

2. **Faire vos modifications** et commits :
```bash
git add .
git commit -m "fix(): description claire du correctif"
```

3. **Pousser votre branche** :
```bash
git push origin bugfix/nom-du-bug
```

4. **Créer une Pull Request (PR)** :
   - Allez sur GitHub
   - Créez une PR depuis votre branche vers `main`
   - Ajoutez une description claire des modifications
   - Ajoutez le label approprié (`bug`, `bugfix`, etc.)

5. **Review et merge** :
   - Attendez l'approbation d'un autre membre de l'équipe
   - Une fois approuvée, mergez la PR
   - Supprimez la branche après le merge

### Conventions de commit

Utilisez des messages de commit clairs et descriptifs :

- `fix(): [description]` pour les corrections de bugs
- `feat(): [description]` pour les nouvelles fonctionnalités
- `docs(): [description]` pour la documentation
- `test(): [description]` pour les tests

**Exemple :**
```bash
git commit -m "fix(): corriger la division entière pour utiliser // au lieu de /"
```

## 📝 Issues

Pour signaler un bug ou proposer une amélioration :

1. Allez dans l'onglet "Issues" sur GitHub
2. Cliquez sur "New issue"
3. Choisissez le template approprié (Bug report, Feature request)
4. Remplissez les informations demandées
5. Ajoutez les labels appropriés

## 📂 Structure du projet
```
TP3---LOG3000/
│
├── app.py                   # Application Flask principale
├── operators.py             # Fonctions des opérations arithmétiques
├── requirements.txt         # Dépendances Python
├── README.md               # Ce fichier (documentation principale)
│
├── static/                 # Fichiers statiques
│   ├── style.css          # Styles CSS de l'application
│   └── README.md          # Documentation du dossier static
│
├── templates/              # Templates HTML Jinja2
│   ├── index.html         # Page principale de la calculatrice
│   └── README.md          # Documentation du dossier templates
│
└── tests/                  # Tests unitaires
    ├── conftest.py        # Configuration pytest
    ├── test_operators.py  # Tests des opérations arithmétiques
    └── README.md          # Documentation des tests
```

## 📄 Licence

Ce projet est développé dans le cadre du cours LOG3000 à Polytechnique Montréal.
