class BankError(Exception):
    amount: int
    balance: int

    def __init__(self, message: str, balance: int, amount: int,*args):
        super().__init__(message)
        self.amount = amount
        self.balance = balance

class InvalidAmountError(BankError):
    pass

class InsufficientFundsError(BankError):
    pass

def withdraw(balance: int, amount: int):
    if amount <= 0:
        raise InvalidAmountError("Можно снимать только положительную сумму ", balance, amount)
    if balance < amount:
        raise InsufficientFundsError('Недостаточно средств', balance, amount)
    return balance - amount

def call_with_error():
    withdraw(200,500)

try:
    call_with_error()

except InvalidAmountError as e:
    print('Получена ошибка некорректоной суммы', e)
    print('Текущий баланс', e.balance)
    print('Сумма снятия', e.amount)

except InsufficientFundsError as e:
    print('Получена ошибка счёта', e)
    print('Текущий баланс', e.balance)
    print('Сумма снятия', e.amount)

except BankError as e:
    print('Получена другая ошибка банковского счёта', e)
    print('Текущий баланс', e.balance)
    print('Сумма снятия', e.amount)