numbers = []
with open("numbers.txt","r",encoding='utf-8') as file:
    for line in file:
        line = line.rstrip("\n")
    try:
        number = int(line)
        numbers.append(number)
    except ValueError:
        print(f'Пропущена строка: {line}')
if numbers:
    minn = min(numbers)
    maxx = max(numbers)
    average = sum(numbers) / len(numbers)

    with open('result.txt','w',encoding='utf-8') as file:
        file.write(f'Минимум:{minn}\n')
        file.write(f'Максимум:{maxx}\n')
        file.write(f'Среднее значение:{average}\n')
else:
    print('В файле нет корректных чисел')