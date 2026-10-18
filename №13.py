import time
from contextlib import contextmanager

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.perf_counter()
        print(f"[Класс] Время: {self.end - self.start:.6f} сек")
        return False


@contextmanager
def timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f"[Функция] Время: {end - start:.6f} сек")


def some_function():
    total = 0
    for i in range(1_000_000):
        total += i
    return total

print("Запуск через класс:")
with Timer():
    some_function()

print("\nЗапуск через декоратор:")
with timer():
    some_function()