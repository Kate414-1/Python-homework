import time
import random
import functools
def retry(attempts):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  [Попытка {attempt}/{attempts}] Ошибка: {e}")
                    if attempt == attempts:
                        raise e
                    time.sleep(0.5)
        return wrapper
    return decorator

@retry(5)
def load_data():
    print("  Попытка загрузить данные...")
    if random.random() < 0.5:
        raise ConnectionError("Сбой сети!")
    print("  Успешно загружено!")
    return "Данные"

print("--- Запуск ---")
try:
    result = load_data()
    print("Результат:", result)
except ConnectionError as e:
    print("Функция окончательно упала с ошибкой:", e)