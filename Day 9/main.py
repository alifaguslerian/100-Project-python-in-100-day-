# Day 9 - Check Ingredients

recipe_ingredients = {"flour", "sugar", "butter", "eggs", "milk"}

user_input = input("Enter the ingredients you have (separated by commas): ")
user_ingredients = set(item.strip() for item in user_input.split(","))  # biar spasi ga ngaruh

missing_ingredients = recipe_ingredients - user_ingredients
extra_ingredients = user_ingredients - recipe_ingredients

print("\n--- Ingredient Check Result ---")
if missing_ingredients:
    print(f"You are missing the following ingredients: {', '.join(missing_ingredients)}")
else:
    print("✅ You have all the ingredients needed for the recipe!")

if extra_ingredients:
    print(f"You have extra ingredients: {', '.join(extra_ingredients)}")
else:
    print("No extra ingredients detected.")
