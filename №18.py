import re
import json
import logging
logging.basicConfig(
    level=logging.INFO,
    filename='processing.log',
    filemode='w',
    encoding='utf-8'
)
methods_count = {}
errors_4xx = 0
urls_count = {}
try:
    logging.info("Начало обработки")
    with open("access.log", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            match = re.search(r'(\d+\.\d+\.\d+\.\d+)\s+(\w+)\s+(\S+)\s+(\d{3})', line)
            if match:
                ip = match.group(1)
                method = match.group(2)
                url = match.group(3)
                status = int(match.group(4))
                methods_count[method] = methods_count.get(method, 0) + 1
                urls_count[url] = urls_count.get(url, 0) + 1

                if 400 <= status <= 499:
                    errors_4xx += 1
                    logging.warning(f"Ошибка {status}: {url}")
    logging.info("Обработка завершена")

except FileNotFoundError:
    logging.error("Файл не найден")
    print("Ошибка: файл access.log не найден")

most_frequent_url = max(urls_count, key=urls_count.get) if urls_count else None

stats = {
    "methods": methods_count,
    "errors_4xx": errors_4xx,
    "most_frequent_url": most_frequent_url
}

with open("stats.json", "w", encoding="utf-8") as f:
    json.dump(stats, f, ensure_ascii=False, indent=4)

logging.info("Статистика сохранена")
print(methods_count)
print(errors_4xx)
print(most_frequent_url)