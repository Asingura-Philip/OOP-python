# Character Class (Encapsulation)
class Character:
    def __init__(self, name, health, position):
        self.__name = name
        self.__health = health
        self.__position = position
        
    # Getter methods
    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    def get_position(self):
        return self.__position
    
    # Setter methods
    def set_position(self, new_position):
        self.__position = new_position
    
    # Methods for character actions
    def move(self, new_position):
        self.set_position(new_position)
        print(f"{self.get_name()} moves to {new_position}")
        
    def attack(self, target):
        print(f"{self.get_name()} attacks {target.get_name()}!")
        
    def interact(self, object):
        print(f"{self.get_name()} interacts with {object.get_name() if isinstance(object, Character) else object.get_type()}")

# Vehicle Class (Encapsulation)
class Vehicle:
    def __init__(self, vehicle_type, speed, fuel_level):
        self.__vehicle_type = vehicle_type
        self.__speed = speed
        self.__fuel_level = fuel_level
        
    # Getter methods
    def get_type(self):
        return self.__vehicle_type
    
    def get_speed(self):
        return self.__speed
    
    def get_fuel_level(self):
        return self.__fuel_level
    
    # Setter method
    def set_fuel_level(self, fuel):
        self.__fuel_level = fuel
    
    # Methods for vehicle actions
    def drive(self):
        if self.get_fuel_level() > 0:
            print(f"Driving the {self.get_type()} at speed {self.get_speed()}.")
            self.__fuel_level -= 1  # Assume fuel consumption per drive
        else:
            print(f"Cannot drive! {self.get_type()} is out of fuel.")
    
    def refuel(self, amount):
        self.set_fuel_level(self.get_fuel_level() + amount)
        print(f"{self.get_type()} refueled. Current fuel level: {self.get_fuel_level()}")
    
    def stop(self):
        print(f"{self.get_type()} has stopped.")

# Extended Character Class with Interaction Methods (Abstraction)
class CharacterWithVehicle(Character):
    def __init__(self, name, health, position):
        super().__init__(name, health, position)
        self.__current_vehicle = None  # No vehicle initially

    # Character interacts with vehicle
    def get_in(self, vehicle):
        if self.__current_vehicle is None:
            self.__current_vehicle = vehicle
            print(f"{self.get_name()} gets into the {vehicle.get_type()}.")
        else:
            print(f"{self.get_name()} is already in a vehicle.")
    
    def get_out(self):
        if self.__current_vehicle is not None:
            print(f"{self.get_name()} gets out of the {self.__current_vehicle.get_type()}.")
            self.__current_vehicle = None
        else:
            print(f"{self.get_name()} is not in a vehicle.")

# Specialized HeroCharacter Class (Inheritance)
class HeroCharacter(CharacterWithVehicle):
    def __init__(self, name, health, position, special_ability):
        super().__init__(name, health, position)
        self.__special_ability = special_ability
    
    def get_special_ability(self):
        return self.__special_ability
    
    # Additional methods for HeroCharacter
    def use_special_ability(self):
        print(f"{self.get_name()} uses their special ability: {self.__special_ability}!")

# Simple Game Scenario (Polymorphism)
def game_scenario():
    # Create Characters
    player1 = CharacterWithVehicle("Orion", 100, (0, 0))  # Use CharacterWithVehicle here
    player2 = HeroCharacter("Pax", 150, (5, 5), "Double Jump")
    
    # Create Vehicles
    car = Vehicle("Car", 80, 10)
    bike = Vehicle("Bike", 60, 5)
    
    # Character Actions
    player1.move((1, 1))
    player1.attack(player2)
    
    # Player1 interacts with a vehicle
    player1.interact(car)
    player1.get_in(car)  # Now player1 can use get_in() because it's an instance of CharacterWithVehicle
    car.drive()
    
    # Player2's special abilities
    player2.use_special_ability()
    
    # Player1 refuels the car
    car.refuel(10)
    
    # Game scenario with interactions
    player1.get_out()
    player1.get_in(bike)
    bike.drive()
    
# Run the game scenario
game_scenario()
