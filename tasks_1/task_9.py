class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_final_price(self):
        return self.price

    def __str__(self):
        return f"{self.name} (Цена: {self.get_final_price()} руб., В наличии: {self.quantity} шт.)"

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_months):
        super().__init__(name, price, quantity)
        self.warranty_months = warranty_months

    def get_final_price(self):
        return self.price * 1.05  # Наценка 5% за гарантию

class Food(Product):
    def __init__(self, name, price, quantity, expiry_date):
        super().__init__(name, price, quantity)
        self.expiry_date = expiry_date

class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, name):
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        return None

    def sell_product(self, name, amount):
        product = self.find_product(name)

        if product is None:
            print(f"Ошибка: Товар '{name}' не найден.")
            return

        if product.quantity < amount:
            print(f"Ошибка: Недостаточно товара '{name}'. В наличии: {product.quantity}, запрошено: {amount}.")
            return

        product.quantity -= amount
        total_price = product.get_final_price() * amount
        print(f"Успешно продано {amount} шт. товара '{name}'. Итого к оплате: {total_price:.2f} руб.")

# --- Проверка работы ---

store = Store()

store.add_product(Book("Война и мир", 1000, 5, "Лев Толстой"))
store.add_product(Electronic("Смартфон", 20000, 10, 12))
store.add_product(Food("Хлеб", 50, 20, "2026-10-20"))

print("1. Продажа книги:")
store.sell_product("Война и мир", 2)

print("\n2. Продажа электроники (с наценкой):")
store.sell_product("Смартфон", 1)

print("\n3. Попытка продать больше, чем есть:")
store.sell_product("Хлеб", 100)

print("\n4. Попытка продать несуществующий товар:")
store.sell_product("Телевизор", 1)

print("\n5. Поиск товара и вывод его информации:")
p = store.find_product("Смартфон")
if p:
    print(p)