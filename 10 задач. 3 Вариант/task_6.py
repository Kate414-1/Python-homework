import random
from datetime import date, timedelta, datetime
PRODUCTS = [
    ("Book", 500),
    ("Pen", 80),
    ("Notebook", 200),
    ("Backpack", 2500),
    ("Pencil", 30),
]

def make_file(filename, n=5000):
    start = date(2026, 1, 1)
    end = date(2026, 3, 31)
    days = (end - start).days

    with open(filename, "w", encoding="utf-8") as f:
        f.write("date,product,quantity,price\n")
        for _ in range(n):
            if random.random() < 0.05:
                f.write("bad,line,here\n")
                continue
            d = start + timedelta(days=random.randint(0, days))
            name, price = random.choice(PRODUCTS)
            qty = random.randint(1, 10)
            f.write(f"{d.isoformat()},{name},{qty},{price}\n")

def analyze(filename):
    total = 0
    count = 0
    by_product = {}
    by_day = {}
    with open(filename, "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            date_str, product, qty_str, price_str = parts
            try:
                d = datetime.strptime(date_str, "%Y-%m-%d").date()
                qty = int(qty_str)
                price = float(price_str)
            except ValueError:
                continue
            revenue = qty * price
            total += revenue
            count += 1
            if product not in by_product:
                by_product[product] = [0, 0]
            by_product[product][0] += qty
            by_product[product][1] += revenue
            by_day[d] = by_day.get(d, 0) + revenue
    if count == 0:
        return None
    top_qty = None
    top_qty_num = -1
    top_money = None
    top_money_num = -1
    for name in by_product:
        qty = by_product[name][0]
        money = by_product[name][1]
        if qty > top_qty_num:
            top_qty_num = qty
            top_qty = name
        if money > top_money_num:
            top_money_num = money
            top_money = name
    top_day = None
    top_day_num = -1
    for d in by_day:
        if by_day[d] > top_day_num:
            top_day_num = by_day[d]
            top_day = d
    return {
        "total": total,
        "count": count,
        "avg": total / count,
        "top_qty": top_qty,
        "top_money": top_money,
        "top_day": top_day,
    }

def main():
    make_file("sales.csv", 5000)
    result = analyze("sales.csv")
    if result is None:
        print("Нет корректных записей.")
        return
    print("Общая сумма продаж:        ", round(result["total"], 2))
    print("Корректных записей:        ", result["count"])
    print("Средняя стоимость покупки: ", round(result["avg"], 2))
    print("Самый продаваемый товар:   ", result["top_qty"])
    print("Товар с макс. выручкой:    ", result["top_money"])
    print("День с макс. выручкой:     ", result["top_day"])

if __name__ == "__main__":
    main()