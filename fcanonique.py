def logical_function(x, y, z):
    """
    Exemple de fonction logique (ET à 3 variables).
    """
    return x and y and z

def generate_truth_table(logical_function):
    """
    Génère la table de vérité pour la fonction logique donnée.
    """
    truth_table = []
    for x in (False, True):
        for y in (False, True):
            for z in (False, True):
                output = logical_function(x, y, z)
                truth_table.append((x, y, z, output))
    return truth_table

def minterms(truth_table):
    """
    Récupère les mintermes de la fonction logique.
    """
    minterms = []
    for row in truth_table:
        if row[3]:  # Si la sortie est vraie (1)
            minterm = []
            for i, value in enumerate(row[:3]):
                if value:  # Si la variable est vraie (1)
                    minterm.append(f"x{i}")
                else:  # Si la variable est fausse (0)
                    minterm.append(f"~x{i}")
            minterms.append("".join(minterm))
    return minterms

def maxterms(truth_table):
    """
    Récupère les maxterms de la fonction logique.
    """
    maxterms = []
    for row in truth_table:
        if not row[3]:  # Si la sortie est fausse (0)
            maxterm = []
            for i, value in enumerate(row[:3]):
                if value:  # Si la variable est vraie (1)
                    maxterm.append(f"~x{i}")
                else:  # Si la variable est fausse (0)
                    maxterm.append(f"x{i}")
            maxterms.append(" + ".join(maxterm))
    return maxterms

# Générer la table de vérité
truth_table = generate_truth_table(logical_function)

# Afficher la table de vérité
print("Table de vérité :")
for row in truth_table:
    print(row)

# Récupérer les mintermes et les maxterms
minterms = minterms(truth_table)
maxterms = maxterms(truth_table)

# Afficher la première forme canonique (somme de produits)
print("\nPremière forme canonique (somme de produits) :")
print(" + ".join(minterms))

# Afficher la deuxième forme canonique (produit de sommes)
print("\nDeuxième forme canonique (produit de sommes) :")
print(" * ".join(maxterms))