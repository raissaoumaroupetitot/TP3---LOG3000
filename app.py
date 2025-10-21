from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Mapping des opérateurs texte aux fonctions implémentant l'opération
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évaluer une expression arithmétique.

    Paramètres
    - expr (str): chaîne représentant une opération binaire simple.

    Retour
    - float: résultat numérique de l'opération.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Normaliser : enlever les espaces pour simplifier la recherche d'opérateur
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Chercher la position du premier (et seul) opérateur connu dans la chaîne
    for i, ch in enumerate(s):
        if ch in OPS:
            # Si on trouve déjà un opérateur, l'expression est ambigüe (ex: "1+2-3")
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Vérifier que l'opérateur existe et n'est pas en bordure (ex: "+3" ou "3+")
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    # Convertir les opérandes en float; lever une erreur claire en cas d'échec
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Déléguer l'opération à la fonction correspondante dans OPS
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route de la page principale.

    GET: rend le template de l'interface utilisateur avec un champ de résultat vide.
    POST: récupère le champ 'display' du formulaire, appelle `calculate` et renvoie
          le résultat ou un message d'erreur à afficher dans le template.

    Retour
    - rendu du template 'index.html' avec le resultat correct (float).
    ou
    - rendu du template 'index.html' avec un message d'erreur à afficher dans le template (string)
    """
    result = ""
    if request.method == 'POST':
        # Récupération sécurisée de la valeur envoyée par le formulaire
        expression = request.form.get('display', '')
        try:
            # `calculate` peut lever ValueError; on capture ici pour afficher l'erreur
            result = calculate(expression)
        except Exception as e:
            # Ne pas révéler des détails sensibles en prod; ici on renvoie un message lisible pour dev
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
