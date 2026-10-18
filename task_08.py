def read_file(path):
    try:
        with open(path,"r",encoding="utf-8") as f:
            return f.read()

    except FileNotFoundError:
        print("Ошибка: отсутствие файла")

    except PermissionError as e:
        print(f"Ошибка: нет прав доступа{e}")

    except Exception as e:
        print(f"Ошибка: {e.__class__.__name__}")
read_file(input())