# Щоб перетворити ітератор на генератор,
# ми можемо використати функцію з ключовим словом yield
# замість класу з методами __iter__() та __next__()
# Генератор автоматично веде облік свого стану в місці кожного виклику yield
# і відновлює виконання з цього місця при наступному виклику.

# Генератор - це функція, яка дозволяє декларативно створювати ітератор
# за допомогою ключового слова yield . Він автоматично
# реалізує методи __iter__() та __next__(), тому більше не потрібно їх явно визначати.
# Створення генератора - це просто написання функції,
# яка використовує yield для повернення наступного значення


from random import randint


def rand_generator(start, end, quantity):
    count = 0
    while count < quantity:
        yield randint(start, end)
        count += 1


if __name__ == '__main__':
    for rn in rand_generator(1, 20, 5):
        print(rn, end=' ')
