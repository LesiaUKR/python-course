# Асоціація в ООП - це відношення між об'єктами, які вказують на те,
# що один об'єкт використовує інший об'єкт як частину свого стану.

# Асоціація поділяється на два основних типи: композиція та агрегація,
# кожен з яких має свої особливості та застосування.
class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self) -> str:
        return f"It's animal. His name is {self.nickname} and he's {self.age} years old"


class Owner:
    def __init__(self, name, phone) -> None:
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"

# Composition Owner та Animal


class Cat(Animal):
    def __init__(self, nickname: str, age: int, name: str, phone: str) -> None:
        super().__init__(nickname, age)
        self.owner = Owner(name, phone)

    def get_info(self) -> str:
        return f"It's cat. His name is {self.nickname} and he's {self.age} years old"

    def sound(self) -> str:
        return f"{self.nickname} says Meow!"


cat = Cat("Simon", 4, "Yurii", "+380509993524")
print(cat.owner.info())
