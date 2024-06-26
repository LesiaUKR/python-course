
# utf-16, utf-8, ascii, cp1251
# try with x
file = open("test.txt", "a", encoding="utf-8")  # append
file.write("The end!\n")
file.write("It still end!\n")
file.close()

# перетворення рядка у байт-рядок
byte_str = 'some text'.encode()
print(byte_str)
str.encode(encoding="utf-8", errors="strict")
# encoding - вказує метод кодування. По замовчуванню використовується 'utf-8',
# який підтримує велику кількість символів з різних мов.
# errors - вказує, як обробляти помилки кодування.
# Наприклад, 'strict' для викидання виключення у випадку помилки,
# 'ignore' для ігнорування помилок або 'replace' для заміни
# неможливих для кодування символів на певний замінник (?).


# UTF-8 - Python за замовчуванням використовує кодування UTF-8 для роботи з рядками
# UTF-8 - один символ може займати від 1 до 4 байт, і всього в алфавіті може бути до 1 112 064 знаків

# CP-1251 - Windows за замовчуванням використовує кодування CP-1251 (також відоме як Windows-1251),
# яке є стандартним для багатьох країн, де використовується кирилиця.

# ord() - функція, яка повертає числове представлення символу UTF-8
ord('a')  # 97

# chr() - функція, яка повертає символ за його числовим представленням UTF-8
chr(128)  # 'd'

# Python може працювати з дуже великою кількістю різних кодувань
s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}")  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82!'

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}")  # b'\xff\xfeP\x00r\x00i\x00v\x00\x1c\x04!\x00'

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}")  # b'\xcf\xf0\xe8\xe2\xe0!'

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s)  # True
