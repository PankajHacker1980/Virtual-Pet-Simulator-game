import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(5, 15)
        self.health = random.randint(5, 15)
        self.energy = random.randint(5, 15)
    
    def display_stats(self):
        print(f"\n{name}'s Stats:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Happiness: {self.happiness}/15")
        print(f"Health: {self.health}/15")
        print(f"Energy: {self.energy}/15")
    
    def feed(self):
        print(f"You feed {self.name}.")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(15, self.happiness + 1)
        self.health = min(15, self.health + 1)
    
    def play(self):
        print(f"You play with {self.name}.")
        self.hunger = min(10, self.hunger + 1)
        self.happiness = min(15, self.happiness + 2)
        self.energy = max(0, self.energy - 2)
    
    def heal(self):
        print(f"You take {self.name} to the vet for healing.")
        self.health = min(15, self.health + 3)
        self.energy = max(0, self.energy - 1)
    
    def sleep(self):
        print(f"You put {self.name} to bed for a nap.")
        self.energy = min(15, self.energy + 4)
        self.hunger = min(10, self.hunger + 1)
    
    def update(self):
        # Pet's stats change over time
        self.hunger = min(10, self.hunger + 1)
        self.happiness = max(0, self.happiness - 1)
        self.health = max(0, self.health - 1)
        self.energy = max(0, self.energy - 1)
    
    def is_alive(self):
        # Check if the pet is alive based on its health
        return self.health > 0

def print_menu():
    print("\nActions:")
    print("1. Feed")
    print("2. Play")
    print("3. Heal")
    print("4. Sleep")
    print("5. Quit")

if __name__ == "__main__":
    name = input("Enter a name for your virtual pet: ")
    pet = VirtualPet(name)
    print(f"\nWelcome to Virtual Pet Simulator! Meet {name}.")

    while pet.is_alive():
        pet.display_stats()
        print_menu()
        choice = input("What do you want to do? (1-5): ").strip()
        
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.heal()
        elif choice == "4":
            pet.sleep()
        elif choice == "5":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

        pet.update()

    if not pet.is_alive():
        print(f"{pet.name} has passed away. Game over.")
