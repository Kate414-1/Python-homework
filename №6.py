import pathlib
p = pathlib.Path(".")
file_count = 0
dir_count = 0
py_files = []
total_size = 0

for item in p.iterdir():
    if item.is_file():
        file_count += 1
        total_size += item.stat().st_size
        if item.suffix == ".py":
            py_files.append(item.name)
    elif item.is_dir():
        dir_count += 1

print(f"Количество файлов: {file_count}")
print(f"Количество подкаталогов: {dir_count}")
print(f"Список .py файлов: {py_files}")
print(f"Суммарный размер всех файлов: {total_size} байт")
