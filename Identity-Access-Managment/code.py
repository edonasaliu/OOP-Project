class User:
    def __init__(self, username):
        self.username = username
        self.courses = {}

    def assign_role(self, course, role):
        self.courses[course] = role

    def can_perform_action(self, action, course):
        if course not in self.courses:
            return False
        return self.courses[course].can_perform_action(action)


class Role:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = set(permissions)

    def can_perform_action(self, action):
        return action in self.permissions


class Student(Role):
    def __init__(self):
        super().__init__("Student", ["view"])


class Professor(Role):
    def __init__(self):
        super().__init__("Professor", ["view", "send_to_breakout", "manage_students"])


class TechSupport(Role):
    def __init__(self):
        super().__init__(
            "TechSupport",
            ["view", "send_to_breakout", "manage_students", "resolve_issues"],
        )


class Course:
    def __init__(self, name):
        self.name = name
        self.users = []

    def add_user(self, user, role):
        user.assign_role(self, role)
        self.users.append(user)


# Creating roles
student_role = Student()
professor_role = Professor()
tech_support_role = TechSupport()

# Creating users
alice = User("Alice")
bob = User("Bob")
charlie = User("Charlie")

# Creating courses
math101 = Course("Math 101")
physics201 = Course("Physics 201")

# Assigning roles to users in courses
math101.add_user(alice, student_role)
math101.add_user(bob, professor_role)
physics201.add_user(charlie, tech_support_role)

# Checking permissions
print(alice.can_perform_action("send_to_breakout", math101))  # False
print(bob.can_perform_action("send_to_breakout", math101))  # True
print(charlie.can_perform_action("resolve_issues", physics201))  # True
