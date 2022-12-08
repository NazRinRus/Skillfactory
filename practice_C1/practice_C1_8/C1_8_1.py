from Cat import Cat

cat1 = Cat(name = 'Сэм', sex = 'мальчик', age = 2)

print(cat1.get_name())
print(cat1.get_sex())
print(cat1.get_age())

class Dog(Cat):
    def get_pet(self):
        return f'{self.get_name()} {self.get_age()}'

dog_1=Dog("Felix","boy",2)

print(dog_1.get_pet())