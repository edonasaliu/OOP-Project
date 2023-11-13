# Identity Access Management System

## Overview

The Identity Access Management (IAM) System is designed to manage access control for a forum-like platform, specifically handling different roles and permissions for students, professors, and tech support personnel across various courses. The system is implemented in Python, showcasing the use of object-oriented programming principles, particularly inheritance and composition.

## Classes and Inheritance

### Role Class

The `Role` class serves as the base class for different roles in the system, defining common properties such as `name` and `permissions`, as well as a method `can_perform_action` to check if a role has a specific permission.

### Student, Professor, and TechSupport Classes

These classes inherit from the `Role` class, demonstrating the use of inheritance. They inherit common properties and methods, and define specific permissions for each role. For example, the `Professor` class includes permissions like 'send_to_breakout' and 'manage_students'.

## Composition

### User Class

The `User` class represents individuals on the platform, containing a dictionary of `courses` associated with roles, showcasing composition. This design allows users to be part of multiple courses with different roles in each, providing flexibility and dynamic role assignment.

### Course Class

The `Course` class represents a course on the platform, containing a list of `users`. This is another example of composition, as courses are composed of multiple users.

## Usage

1. Create instances of role classes (e.g., `Student`, `Professor`, `TechSupport`).
2. Create instances of the `User` class for each individual.
3. Create instances of the `Course` class for each course.
4. Assign roles to users in courses using the `add_user` method of the `Course` class.
5. Check permissions for actions using the `can_perform_action` method of the `User` class.

## Conclusion

The Identity Access Management System effectively demonstrates the use of inheritance and composition in object-oriented programming. Inheritance is used to create a hierarchy of roles, capturing shared properties and behaviors. Composition is used to manage the relationships between users, courses, and roles, providing a flexible and efficient system for access control.