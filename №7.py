import pathlib
directory = input()
exten = input()

a = pathlib.Path(directory)
if not a.exists() or not a.is_dir():
    print("Ошибка!")
else:
    for i in a.rglob(f"*{exten}"):
        if i.is_file():
            print(str(i.absolute()))
            print(i.stat().st_size)