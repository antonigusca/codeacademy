# class Person:
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def say_hello(self):
#         print(f"hello, {self.name}")
#
#
# PERSON = Person("first", "person")
# PERSON.say_hello()
# def x(a):
#     """Function greets a person given full name as a string"""
#
#     print(f"Hello {a.split()[0]} {a.split()[1]}, How are you today?")
def greet_user(age):

    eligieble_to_enter = age > 21

    if eligieble_to_enter:
        print("Welcome")

    if not eligieble_to_enter:
        print("Access denied")
