import heapq
import time
from datetime import datetime, timedelta

class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.created_at = datetime.now()

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"[Приоритет {self.priority}] {self.title}"

class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.delayed_tasks = []

    def add_task(self, title, priority=3):
        task = Task(title, priority)
        heapq.heappush(self.tasks, task)
        print(f"Добавлена задача: {title} (Приоритет: {priority})")

    def add_delayed_task(self, title, priority, delay_seconds):
        execute_time = datetime.now() + timedelta(seconds=delay_seconds)
        task = Task(title, priority)
        self.delayed_tasks.append((execute_time, task))
        print(f"Отложена задача: {title} (Выполнить через {delay_seconds} сек.)")

    def get_next_task(self):
        now = datetime.now()
        for item in self.delayed_tasks[:]:
            execute_time, task = item
            if now >= execute_time:
                self.delayed_tasks.remove(item)
                heapq.heappush(self.tasks, task)
                print(f"  [Система]: Отложенная задача '{task.title}' перемещена в общую очередь.")

        if self.tasks:
            return heapq.heappop(self.tasks)
        return None

    def run_next(self):
        task = self.get_next_task()
        if task:
            print(f"Выполняется: {task.title} (Приоритет: {task.priority})")
        else:
            print("Нет задач для выполнения.")

scheduler = TaskScheduler()

print("--- Добавление задач ---")
scheduler.add_task("Помыть посуду", priority=3)
scheduler.add_task("Сделать уроки", priority=2)
scheduler.add_task("Срочный звонок", priority=1)
scheduler.add_delayed_task("Полить цветы", priority=4, delay_seconds=2)

print("\n--- Выполнение задач по одной ---")
scheduler.run_next()
scheduler.run_next()

print("\n--- Ждем 2 секунды, чтобы отложенная задача стала доступна ---")
time.sleep(2)

print("\n--- Продолжаем выполнение ---")
scheduler.run_next()
scheduler.run_next()
scheduler.run_next()