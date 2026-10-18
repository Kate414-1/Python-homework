with open('text.txt', "r", encoding='utf-8') as file:
    lines = 0
    words = 0
    symbols = 0
    max_lenght = 0
    for line in file:
        line = line.rstrip("\n")
        lines += 1
        words += len(line.split())
        symbols += len(line)
        if len(line) > max_lenght:
            max_lenght = len(line)
print("Количество строк:", lines)
print("Количество слов:", words)
print("Количество символов:", symbols)
print("Длина самой длинной строки:", max_lenght)
