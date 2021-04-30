class Person:
    def __init__(self, age, name, _id):
        self.name = name
        self.age = age
        self._id = _id
        self.__friends = {}
    def know(self, other):
        self.__friends.setdefault(other._id, other)
    def is_known(self, other):
        return other._id in self.__friends
    @property
    def friends(self):
        return list(self.__friends.values())

person1 = Person(18, 'Oleg', _id=uuid.uuid4())
person2 = Person(20, 'Ivan', _id=uuid.uuid4())
person3 = Person(20, 'Ivan', _id=uuid.uuid4())

print(person1.is_known(person2))
person1.know(person2)
person1.know(person2)
person1.know(person2)
person1.know(person2)
person1.know(person2)
person1.know(person3)
print(person1.is_known(person2))
print(person1.friends)