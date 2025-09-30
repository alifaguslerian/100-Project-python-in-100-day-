def load_reciep(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            recipes = content.split("\n\n")
            recipes_dict = {}
            for recipe in recipes:
                lines = recipe.split("\n")
                if len(lines) >= 3:
                    name = lines[0].strip()
                    ingredients = lines[1].replace("Ingredients:", "").strip()
                    instructions = lines[2].replace("Instructions:", "").strip()
                    recipes_dict[name] = {"ingredients": ingredients, "instructions": instructions}
            return recipes_dict
    except FileNotFoundError:
        print("File not found.")
        return {}
    
def show_menu():
    print("\n--- Recipe Menu ---")
    print("1. view all recipes")
    print("2. list a recipe")
    print("3. exit")

def view_recipes(recipes):
    name = input("Enter the name of the recipe: ").strip()
    if name in recipes:
        print(f"\n--- {name} ---") 
        print(f"Ingredients: {recipes[name]['ingredients']}")
        print(f"Instructions: {recipes[name]['instructions']}")
    else:
        print(f"Recipe {name} not found.")

recipe_file = "file.txt"
recipes = load_reciep(recipe_file)

while True:
    show_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        view_recipes(recipes)
    elif choice == "2":
        print("list a recipe")
        for name in recipes:
            print(name)
    elif choice == "3":
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-3).")