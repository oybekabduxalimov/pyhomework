from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Represents a generic Animal on the farm.
    """

    def __init__(self, name: str, age: (int, float), sound: str):
     
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, (int, float)) or age < 0:
            raise ValueError("Age must be a non-negative number.")
        if not isinstance(sound, str) or not sound.strip():
            raise ValueError("Sound must be a non-empty string.")

        self.name = name.strip()
        self.age = age
        self.sound = sound.strip()

    @abstractmethod
    def make_sound(self) -> str:
        """Abstract method for making a sound."""
        pass

    @abstractmethod
    def eat(self) -> str:
        """Abstract method for defining eating behavior."""
        pass

    def sleep(self) -> str:
        """Returns a message indicating that the animal is sleeping."""
        return f"{self.name} is sleeping."

    def __str__(self) -> str:
        """String representation of the Animal."""
        return f"{self.name}, Age: {self.age}, Sound: {self.sound}"


class Cow(Animal):
    """Represents a Cow, inheriting from Animal."""

    def __init__(self, name: str, age: (int, float)):
        super().__init__(name, age, "Moo")

    def make_sound(self) -> str:
        return f"{self.name} says {self.sound}!"

    def eat(self) -> str:
        return f"{self.name} is grazing on grass."


class Chicken(Animal):
    """Represents a Chicken, inheriting from Animal."""

    def __init__(self, name: str, age: (int, float)):
        super().__init__(name, age, "Cluck")

    def make_sound(self) -> str:
        return f"{self.name} says {self.sound}!"

    def eat(self) -> str:
        return f"{self.name} is pecking at grains."


class Pig(Animal):
    """Represents a Pig, inheriting from Animal."""

    def __init__(self, name: str, age: (int, float)):
        super().__init__(name, age, "Oink")

    def make_sound(self) -> str:
        return f"{self.name} says {self.sound}!"

    def eat(self) -> str:
        return f"{self.name} is munching on slop."


class Farm:
    """Represents a Farm that holds multiple animals."""

    def __init__(self):
        """Initializes the farm with an empty list of animals."""
        self.animals = []

    def add_animal(self, animal: Animal) -> str:
        """
        Adds an Animal to the farm.

        :param animal: Instance of Animal (Cow, Chicken, Pig, etc.).
        :return: Confirmation message.
        :raises TypeError: If the provided object is not an instance of Animal.
        """
        if not isinstance(animal, Animal):
            raise TypeError("Only instances of Animal can be added.")
        self.animals.append(animal)
        return f"{animal.name} has been added to the farm."

    def feed_animals(self) -> str:
        """Returns messages for feeding all animals."""
        return "\n".join(animal.eat() for animal in self.animals) if self.animals else "No animals on the farm to feed."

    def animal_sounds(self) -> str:
        """Returns messages for all animals making sounds."""
        return "\n".join(animal.make_sound() for animal in self.animals) if self.animals else "No animals on the farm to hear."

    def farm_summary(self) -> str:
        """Returns a summary of all animals on the farm."""
        return "\n".join(str(animal) for animal in self.animals) if self.animals else "The farm is empty."


# Example Usage
if __name__ == "__main__":
    farm = Farm()

    # Adding animals
    try:
        cow = Cow("Bessie", 5)
        chicken = Chicken("Clucky", 2)
        pig = Pig("Porky", 3)

        print(farm.add_animal(cow))      # Output: Bessie has been added to the farm.
        print(farm.add_animal(chicken))  # Output: Clucky has been added to the farm.
        print(farm.add_animal(pig))      # Output: Porky has been added to the farm.

    except ValueError as e:
        print(f"Error adding animal: {e}")

    # Farm summary
    print("\nFarm Summary:")
    print(farm.farm_summary())

    # Feeding animals
    print("\nFeeding Animals:")
    print(farm.feed_animals())

    # Animal sounds
    print("\nAnimal Sounds:")
    print(farm.animal_sounds())

    # Sleeping behavior
    print("\nAnimal Sleeping:")
    print(cow.sleep())  # Output: Bessie is sleeping.
    print(chicken.sleep())  # Output: Clucky is sleeping.
    print(pig.sleep())  # Output: Porky is sleeping.
