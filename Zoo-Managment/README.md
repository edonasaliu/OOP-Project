# Zoo Management System

## Overview

The Zoo Management System is designed to manage a zoo, keeping track of different types of animals and the enclosures they live in. The system is implemented in Python and demonstrates the use of object-oriented programming principles, specifically inheritance and composition.

## Classes and Inheritance

### Animal Class

The `Animal` class serves as the base class for all animals in the zoo. It defines common properties such as `name`, `weight`, and `age`, as well as a method `make_sound` which can be overridden by subclasses.

### Lion, Shark, and Giraffe Classes

These classes inherit from the `Animal` class, demonstrating the use of inheritance. They inherit the common properties and can have additional properties or methods specific to their type. For example, the `Lion` class has an additional property `mane_size` and overrides the `make_sound` method to return "Roar".

### Enclosure Class

The `Enclosure` class represents an animal enclosure in the zoo. It has properties for `temperature_range`, `feeding_schedule`, and a list of `animals`.

### SavannahEnclosure and SharkEnclosure Classes

These classes inherit from the `Enclosure` class, showing inheritance. They use the properties and methods of the `Enclosure` class but can also have additional properties or methods specific to their type.

## Composition

### Animals in Enclosures

The `Enclosure` class contains a list of `animals`, demonstrating composition. This design choice allows for a flexible and dynamic relationship between enclosures and animals. Enclosures can contain multiple animals, and animals can be easily added or removed.

## Usage

1. Create instances of animal classes (e.g., `Lion`, `Shark`, `Giraffe`).
2. Create instances of enclosure classes (e.g., `SavannahEnclosure`, `SharkEnclosure`).
3. Add animals to enclosures using the `add_animal` method of the enclosure instances.
4. Interact with the objects as needed, such as printing information about the enclosures and their animals.

## Conclusion

The Zoo Management System effectively demonstrates the use of inheritance and composition in object-oriented programming. Inheritance is used to create a hierarchy of animals and enclosures, capturing shared properties and behaviors. Composition is used to manage the relationships between enclosures and animals, providing flexibility and ease of management.