total_sum = 0
min_value = None
max_value = None
count = 0
with open('numbers.txt', 'r', encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue
    n = int(line)
    total_sum += n
    count += 1
    if min_value is None or n < min_value:
        min_value = n
    if max_value is None or n > max_value:
        max_value = n
if count > 0:
    average = total_sum / count
    print(f'Сумма:{total_sum}')
    print(f"Минимум: {min_value}")
    print(f"Максимум: {max_value}")
    print(f"Количество чисел: {count}")
    print(f"Среднее: {average}")
else:
    print("Файл пуст.")