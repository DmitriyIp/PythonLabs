import json
from types import SimpleNamespace

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printColored(text, color = 'yellow'):
    match (color):
        case 'yellow':
            color = bcolors.WARNING
        case 'red':
            color = bcolors.FAIL
        case 'bold':
            color = bcolors.BOLD
        case _:
            color = bcolors.ENDC
    print(f"{color}{text}{bcolors.ENDC}")

class Creature:
    def __init__(self, name=None, json=None):
        if (json != None):
            self.name = json.name
        else:
            self.name = name

class Person(Creature):
    def __init__(self, name=None, surname=None, age=None, json=None):
        if (json != None):
            super().__init__(json = json)
            self.surname = json.surname
            self.age = json.age
        else:
            super().__init__(name)
            self.surname = surname
            self.age = age
    def info(self):
        print("Name: {}, Surname: {}, Age: {},".format(self.name, self.surname, self.age), end=' ')

class Student(Person):
    def __init__(self, name=None, surname=None, age=None, faculty=None, direction=None, json=None):
        if (json != None):
            super().__init__(json = json)
            self.faculty = json.faculty
            self.direction = json.direction
        else:
            super().__init__(name, surname, age)
            self.faculty = faculty
            self.direction = direction
    def info(self):
        super().info()
        print("Faculty: {}, Direction: {}".format(self.faculty, self.direction), ' ')

A = Person("Дмитрий", "Ипатов", 19)

B = Student("Роман", "Красовский", 22, "ЭТФ", "ИВТ")
printColored("Original print")
B.info()

# Serialize Object to JSON string
printColored("Serialize Object to JSON string")
jsonString = json.dumps(vars(B))
print(jsonString)

# Deserialize JSON Object
printColored("Deserialize JSON Object")
abc = json.loads(jsonString, object_hook=lambda a:SimpleNamespace(**a))
print("Десериализуем студента с фамилией {} в JSON объект".format(abc.surname))

# Convert JSON Obj to Original obj
printColored("Convert JSON Obj to Original obj")
deOriginale = Student(json=abc)
deOriginale.info()

