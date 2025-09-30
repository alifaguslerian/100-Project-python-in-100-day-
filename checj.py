# Check ingridients

recipe_ingredients = {"flour", "sugar", "butter", "eggs", "milk"}

user_input = input("Enter the ingredients you have (separated by commas): ")
user_ingredients = set(user_input.split(", "))

missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

print("\n--- Ingredient check result ---")
if missing_ingredients:
    print (f"You are missing the following ingredients: {', '.join(missing_ingredients)}")
else:
    print("You have all the ingredents needed.")

if extra_ingredients:
    print(f"You have extra ingredients: {','.join(extra_ingredients)}")
else:
    print("You have all the ingredients needed.")