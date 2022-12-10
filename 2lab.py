import json
from types import SimpleNamespace

class Creature:
    def __init__(self, name=None, json=None):
        self.name = name


class Person(Creature):
    def __init__(self, name=None, surname=None, age=None, json=None):
        super().__init__(name)
        self.surname = surname
        self.age = age
    def info(self):
        print("Name: {}, Surname: {}, Age: {},".format(self.name, self.surname, self.age), end=' ')

class Student(Person):
    def __init__(self, name, surname=None, age=None, faculty=None, direction=None, json=None):
        super().__init__(name, surname, age)
        self.faculty = faculty
        self.direction = direction
    def info(self):
        super().info()
        print("Faculty: {}, Direction: {}".format(self.faculty, self.direction), ' ')

A = Person("Дмитрий", "Ипатов", 19)

B = Student("Роман", "Красовский", 22, "ЭТФ", "ИВТ")
B.info()

# Serialize Object to JSON string
jsonString = json.dumps(vars(B))
print(jsonString)

# Deserialize JSON Object
abc = json.loads(jsonString, object_hook=lambda a:SimpleNamespace(**a))
print("Мы десереализовали эту падлюку ", abc.surname)    



