import csv

def fn_menu():
    print(f"\nMenu :")
    print(f"1. Ajouter les informations d'une recette à la liste")
    print(f"2. Afficher le contenu de la liste")
    print(f"3. Réinitialiser le contenu du fichier")
    print(f"4. Quitter le programme")
    choix = input(f"Entrez votre choix (1, 2, 3 ou 4) : ")
    return choix

def fn_encode_data_recipe():
    nom = input("Entrez le nom de la recette : ")
    ingredients = []
    print("Entrez les ingrédients et leurs quantités (entrez 'fin' pour terminer) :")
    while True:
        ingredient = input("Ingrédient : ")
        if ingredient.lower() == 'fin':
            quantite = input(f"Quantité de {ingredient} (Veuillez préciser la mesure si nécéssaire) : ")
            ingredients.append({"ingrédient": ingredient, "quantité": quantite})

        data_recipe = {
            "nom": nom,
            "ingredients": ingredients,
}
    return data_recipe



def fn_data(): 
    if fn_menu() == 1
fn_menu()