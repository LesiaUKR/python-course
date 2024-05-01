#
def read_lines(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            # strip() - Повертаємо рядок без символу нового рядка і зайвих пробілів по краях
            # yield - використовується для повернення кожного рядка файлу
            yield line.strip()


# Використання генератора для читання рядків з файлу
for line in read_lines("my_file.txt"):
    print(line)
