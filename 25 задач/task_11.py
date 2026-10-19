import re
with open('log.txt', 'r', encoding='utf-8') as f:
    text = f.read()

all_ids = re.findall(r'User (\d+)', text)
print("Все ID:", all_ids)

error_lines = re.findall(r'.*ERROR.*', text)
print("Строки с ERROR:")
for line in error_lines:
    print(" ", line)

error_ids = re.findall(r'ERROR User (\d+)', text)
print("ID с ошибкой:", error_ids)