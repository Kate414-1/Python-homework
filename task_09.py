#Первый способ решения:
def parse_number(value: str):
    if not value:
        raise ValueError("Передана пустая строка")
    if value.isdigit():
        return float(value)
    else:
        if value.count("-") == 1 and value[0] == "-":
            return parse_number(value[1:]) * (-1)
        if value.count(".") == 1 and ''.join(value.split(".")).isdigit():
            return float(value)
        raise TypeError("Строка содержит запретные символы")

n = input()
try:
    print(parse_number(n))
except TypeError as e:
    print('Получена ошибка типа',e)
except ValueError as e:
    print('Получена ошибка значения',e)

# Второй способ решения:
import re
def parse_number(value: str):
    if re.fullmatch(r"-?\d+(\.\d+)?",value):
        return float(value)
    raise ValueError("Строка неверного формата")