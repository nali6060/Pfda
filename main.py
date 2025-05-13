import csv

def fn_menu():
    print("\nMenu :")
    print("1. Afficher le contenu de la liste")
    print("2. Ajouter les informations d'une recette à la liste")
    print("3. Réinitialiser le contenu du fichier")
    print("4. Quitter le programme")
    choix = input("Entrez votre choix (1, 2, 3 ou 4) : ")
    return choix

def fn_encode_data_recipe():
    nom = input("Entrez le nom de la recette Minecraft : ")
    ingredients = []
    print("Entrez les ingrédients et leurs quantités (entrez 'fin' pour terminer) :")
    while True:
        ingredient = input("Ingrédient : ")
        if ingredient.lower() == 'fin':
            break
        quantite = input(f"Quantité de {ingredient} : ")
        ingredients.append({"ingrédient": ingredient, "quantité": quantite})
    
    return {
        "nom": nom,
        "ingredients": ingredients,
    }

def fn_list_data_recipe(data_recipe, list_data_recipe):
    list_data_recipe.append(data_recipe)

def fn_display_list(list_data_recipe):
    if not list_data_recipe:
        print("Aucune recette en mémoire.")
        return

    for idx, recipe in enumerate(list_data_recipe, 1):
        print(f"\nRecette {idx}")
        print(f"Nom : {recipe['nom']}")
        print("Ingrédients :")
        for ingredient in recipe['ingredients']:
            print(f" - {ingredient['ingrédient']} : {ingredient['quantité']}")

def fn_reset_list_data_recipe_to_file(recipe_file):
    y = input("Êtes-vous sûr de vouloir réinitialiser le fichier ? (y/n) : ")
    if y.lower() == "y":
        with open(recipe_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Nom", "Ingrédients"])
        print("Réinitialisation du fichier effectuée.")
    else:
        print("Annulation de la procédure de formatage.")

def fn_write_list_data_recipe_to_file(recipe_file, list_data_recipe):
    with open(recipe_file, "a", newline="") as file:
        writer = csv.writer(file)
        for recipe in list_data_recipe:
            ingredients_str = "; ".join([
                f"{ingredient['ingrédient']}:{ingredient['quantité']}" for ingredient in recipe['ingredients']
            ])
            writer.writerow([recipe['nom'], ingredients_str])
    list_data_recipe.clear()  # vider la liste une fois sauvegardée
    return f"Données enregistrées dans '{recipe_file}'"

def fn_read_recipe_file(recipe_file):
    try:
        with open(recipe_file, "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header:
                print(f"\n{header[0]:<20} | {header[1]}")
                print("-" * 50)
            for row in reader:
                print(f"{row[0]:<20} | {row[1]}")
    except FileNotFoundError:
        print(f"\nERREUR : Le fichier '{recipe_file}' n'existe pas.")

def fn_app():
    script_run = True
    recipe_file = "recettes_minecraft.csv"
    list_data_recipe = []
    
    while script_run:
        choix = fn_menu()
        match choix:
            case "1":
                fn_read_recipe_file(recipe_file)
            case "2":
                data_recipe = fn_encode_data_recipe()
                fn_list_data_recipe(data_recipe, list_data_recipe)
                debug_msg = fn_write_list_data_recipe_to_file(recipe_file, list_data_recipe)
                print(debug_msg)
            case "3":
                fn_reset_list_data_recipe_to_file(recipe_file)
            case "4":
                print("Fermeture de l'application.")
                script_run = False
            case _:
                print("Choix non valide.")

fn_app()
