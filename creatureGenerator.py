import pickle

class Animal:
    def __init__(self, name, height, weight, fact):
        self.name = name
        self.height = height
        self.weight = weight
        self.fact = fact

a1 = Animal("Golden Retriever", 23, 70, "Often used as service dogs")
a2 = Animal("Poodle", 20, 65, "Friendly and intelligent")
a3 = Animal("German Shepperd", 25, 85, "Excellent therapy dogs")
a4 = Animal("Bulldog", 14, 45, "Originally bred to drive cattle")
a5 = Animal("Husky", 22, 55, "Known for their ability to survive extremely cold temperatures")
a6 = Animal("Maine Coon", 15, 22, "Known as 'gentle giants' for their large size but friendly tempermant")
a7 = Animal("Siamese", 9, 9, "Vocal nature and often try to communicate with their owners")
a8 = Animal("Bengal", 9, 11, "Wild appearance and leopard like spots")
a9 = Animal("Cow", 60, 1600, "Specialized intestines with four stomachs")
a10 = Animal("Sheep", 42, 270, "Have excellent memories and could recognize the faces of 50 other sheeps")
a11 = Animal("Goat", 30, 220, "Have rectangular pupils giving them a wide field of view")
a12 = Animal("Horse", 66, 2000, "Have a similar 'flight' instict like humans")
a13 = Animal("Chicken", 18, 6, "Capable of recognizing and remembering 100 different faces (human and animal)")
a14 = Animal("Lion", 48, 400, "Live in social groups called 'prides'")
a15 = Animal("Elephant", 144, 12000, "Largest land animal on earth")
a16 = Animal("Giraffe", 204, 2800, "Have long necks with 7 vertebrae")
a17 = Animal("Hippo", 54, 3500, "Spend most of their day submerged in water")
a18 = Animal("Rhinoceros", 72, 4000, "Their horns are made of keratin, the same substance as human hair and nails")
a19 = Animal("Tiger", 42, 400, "Distinctive orange coat with black stripes")
a20 = Animal("Gorilla", 42, 420, "Complex social structure led by a dominant male Silverback")
a21 = Animal("Shark", 60, 2000, "Can sense a drop of blood in 25 gallons of water")
a22 = Animal("Whale", 960, 300000, "Largest animal ever known to have existed, heart can weigh as much as a car")
a23 = Animal("Squid", 456, 600, "Eight arms and two tenticles")
a24 = Animal("Octopus", 30, 21, "Highly intelligent and can change their color in order to adapt")
a25 = Animal("Sea Turtle", 24, 300, "Navigate using earths magnetic field")
a26 = Animal("T-Rex", 216, 18000, "Strongest bite force of any terrestrial animal")
a27 = Animal("Triceratops", 120, 22000, "Used its horn and frill as a defensive mechanism")
a28 = Animal("Velociraptor", 24, 30, "Recent studies suggest that the velociraptor was more closely related to birds")
a29 = Animal("Dragon", 336, 19000, "Across cultures, they all share common traits like the ability to fly and breath fire")
a30 = Animal("Unicorn", 66, 1300, "Resembles a horse, except it has evolved into a majestic, golden horse")

animals_list = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30]

def add_animal(animals_list):
    name = input("Enter the animal's name: ")
    height = float(input("Enter the animal's height (in inches): "))
    weight = float(input("Enter the animal's weight (in pounds): "))
    fact = input("Enter an interesting fact about the animal: ")
    new_animal = Animal(name, height, weight, fact)
    animals_list.append(new_animal)
    print(f"{new_animal.name} added successfully!")

def display_animals(animals_list):
    if not animals_list:
        print("No animals have been added yet.")
    else:
        print("\nList of All Animals:")
        for animal in animals_list:
            print(f"Name: {animal.name}, Height: {animal.height} inches, Weight: {animal.weight} pounds, Fact: {animal.fact}")

def save_file(animals_list):
    filename = input("Enter the filename to save your animals: ")
    if not filename.endswith('.pickle'):
        filename += '.pickle'
    with open(filename, 'wb') as f:
        pickle.dump(animals_list, f)
    print("Animals saved successfully to", filename)

def load_file():
    from os import listdir
    save_files = [f for f in listdir() if f.endswith('.pickle')]
    
    if not save_files:
        print("No saved files found. Starting with precreated animals.")
        return [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30]

    print("Select a file to load:")
    for i, file in enumerate(save_files):
        print(f"{i + 1}: {file}")

    try:
        file_choice = int(input("Choose a file to load, or press any key to start a new one: ")) - 1
        if 0 <= file_choice < len(save_files):
            with open(save_files[file_choice], 'rb') as f:
                return pickle.load(f)
        else:
            print("Invalid file selection. Loading precreated animals.")
            return [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30]
    except ValueError:
        print("Loading precreated animals.")
        return [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30]

def combine_names(name1, name2):
    split1 = name1.split()
    split2 = name2.split()
    
    prefix1 = split1[0]
    suffix1 = split1[-1]
    prefix2 = split2[0]
    suffix2 = split2[-1]

    combined_name = f"{prefix1[:len(prefix1)//2]}{suffix2}"
    
    return combined_name.capitalize()

def combine_animals(animals_list):
    if len(animals_list) < 2:
        print("Not enough animals to combine.")
        return
    
    print("Select two animals to combine:")
    for i, animal in enumerate(animals_list):
        print(f"{i + 1}. {animal.name}")
    
    try:
        choice1 = int(input("Enter the number of the first animal: ")) - 1
        choice2 = int(input("Enter the number of the second animal: ")) - 1
        
        if (0 <= choice1 < len(animals_list)) and (0 <= choice2 < len(animals_list)) and (choice1 != choice2):
            animal1 = animals_list[choice1]
            animal2 = animals_list[choice2]
            
            combined_name = combine_names(animal1.name, animal2.name)
            combined_height = (animal1.height + animal2.height) / 2
            combined_weight = (animal1.weight + animal2.weight) / 2
            combined_fact = f"{animal1.fact} and {animal2.fact}"
            
            combined_animal = Animal(combined_name, combined_height, combined_weight, combined_fact)
            animals_list.append(combined_animal)
            print(f"Combined animal created: {combined_animal.name}")
            print(f"Combined height: {combined_animal.height}")
            print(f"Combined weight: {combined_animal.weight}")
            print(f"Combined fact: {combined_animal.fact.capitalize()}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main_menu():
    animals_list = load_file()
    if not animals_list:
        animals_list = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30] 

    while True:
        print("\nMain Menu:")
        print("1. Display All Animals")
        print("2. Combine 2 Animals")
        print("3. Add an Animal")
        print("4. Save File")
        print("5. Load File")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_animals(animals_list)
        elif choice == '2':
            combine_animals(animals_list)
        elif choice == '3':
            add_animal(animals_list)
        elif choice == '4':
            save_file(animals_list)
        elif choice == '5':
            animals_list = load_file()
            if not animals_list:
                animals_list = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30]
            print("Animals loaded successfully.")
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
