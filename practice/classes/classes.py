
class Person:

    def __init__(self, age, name) -> None:
        self.age = age
        self.name = name

    def __str__(self) -> str:
        return f"I am {self.name}"
    
    def __gt__(self, person2) -> bool:

        return True if self.age>person2.age else False


luis = Person(name="luis",age =30)
print(luis)
susana = Person(name="susana", age = 26)

print(susana>luis)


[19,29,88,2,5,24,60,26,76,24,96,82,97,97,72,35,21,77,82,30,94,55,76,94,51,82,3,89,52,96,72,27,59,57,97,6,46,88,41,52,46,4,17]