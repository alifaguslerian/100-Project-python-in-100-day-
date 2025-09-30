# Animal sound simulator

class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

class dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")

class duck(Animal):
    def make_sound(self):
        print("Quack!")

# Create instances of different animals
class AnimalSoundSimulator:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"Added {type(animal).__name__} to the simulator.")
        else:
            print("Invalid animal type. Please provide an Animal instance.")

    def make_all_sounds(self):
        if not self.animals:
            print("No animals added to the simulator.")
        else:
            print("\n--- Animal Sounds ---")
            for animal in self.animals:
                animal.make_sound()

# Main program
simulator = AnimalSoundSimulator()

while True:
    print("\n--- Animal Sound Simulator ---")
    print("1. Add dog")
    print("2. Add cat")
    print("3. Add cow")
    print("4. Add duck")
    print("5. Make all animals sound")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        simulator.add_animal(dog())
    elif choice == "2":
        simulator.add_animal(Cat())
    elif choice == "3":
        simulator.add_animal(Cow())
    elif choice == "4":
        simulator.add_animal(duck())
    elif choice == "5":
        simulator.make_all_sounds()
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-6).")