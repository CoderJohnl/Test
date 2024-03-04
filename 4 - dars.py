

class Employees:
    def __init__(self, id, name, lastname, age, email):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email


# employees = [
#     (1, 'Toxir', "Toxirov", 27, "toxirov@gmail.com"),
#     (2, 'Sobir', "Toxirov", 23, "sobirov@gmail.com")
# ]
#
#
# for employee in employees:
#     em = Employees(*employee)
#     print(em.id, em.name, em.lastname, em.age, em.email)


# from collections import namedtuple
# Employees = namedtuple("Employee", "id name lastname age email")
# employees = [
#     (1, 'Toxir', "Toxirov", 27, "toxirov@gmail.com"),
#     (2, 'Sobir', "Toxirov", 23, "sobirov@gmail.com")
# ]
# for employee in employees:
#     em = Employee(*employees)
#     print(em.id, em.name, em.lastname, em.age, em.email









# class Car:
#         def __init__(self, id, model, color, speed, price):
#             self.id = id
#             self.model = model
#             self.color = color
#             self.speed = speed
#             self.price = price

from collections import namedtuple
Car = namedtuple("Car", "id model color speed price")


cars = [
    (1, "BMW", "Blue", 250, 50000),
    (2, "Chevrolet", "Black", 200, 20000),
    (3, "Mersades", "Black", 300, 55000)
]
for car in cars:
    c = Car(*car)
    print(c.id, c.model, c.speed, c.price)