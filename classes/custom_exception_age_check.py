class MyCustomError(Exception):
    """Базовий клас для власних винятків"""
    pass

# Визначення власного класу винятку


class AgeVerificationError(Exception):
    def __init__(self, message="Вік не задовольняє мінімальній вимозі"):
        self.message = message
        super().__init__(self.message)

# Функція для перевірки віку


def verify_age(age: int):
    if age < 18:
        raise AgeVerificationError("Вік особи меньший за 18 років")


if __name__ == "__main__":
    # Обробка винятку
    try:
        verify_age(21)  # Змініть вік для різних результатів
    except AgeVerificationError as e:
        print(f"Виняток: {e}")
    else:
        print("Вік перевірено, особа доросла.")
