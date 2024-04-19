import math

# Пакет math у Python надає доступ до математичних функцій, визначених стандартом мови C.
# Цей пакет включає функції для різних математичних операцій,
# включаючи тригонометричні обчислення, логарифми, квадратний корінь та інше.

# Константи:

# math.pi - константа π (приблизно 3.14159...);
# math.e - константа e, основа натуральних логарифмів (приблизно 2.71828...);
# math.tau - константа τ, дорівнює 2π (приблизно 6.28318...);
# math.inf - позначення нескінченності;
# math.nan - позначення 'Not a Number' (не число);

# Використання констант
print(math.pi)  # Виведе приблизне значення π

# Вихідне число
x = 3.7

# Використання різних методів округлення
ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини

print(ceil_result, floor_result, trunc_result)  # 4 3 3


# Тригонометричні функції
# math.sin(x) - синус x, де x в радіанах;
# math.cos(x) - косинус x;
# math.tan(x) - тангенс x;
# math.asin(x) - арксинус x;
# math.acos(x) - арккосинус x;
# math.atan(x) - арктангенс x;

# Тригонометрія
angle = math.radians(60)  # Конвертація з градусів у радіани
print(math.sin(angle))  # Синус кута 60 градусів

# Експоненційні та логарифмічні функції
# math.exp(x) - число e в ступені x;
# math.log(x[, base]) - Логарифм x за основою base. Якщо base не вказано, обчислюється натуральний логарифм;

# Логарифми
print(math.log(10, 2))  # Логарифм 10 за основою 2

# Ступінь та корінь
# math.pow(x, y) - x у ступені y;
# math.sqrt(x) - квадратний корінь з x;

# Корінь числа
print(math.sqrt(9))  # Квадратний корінь з 9

# Деякі інші функції
# math.fabs(x) - модуль (абсолютне значення) x;
# math.factorial(x) - факторіал числа x;
# math.gcd(x, y) - найбільший спільний дільник для x та y;