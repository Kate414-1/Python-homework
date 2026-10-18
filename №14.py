class log_operation:
    def __init__(self, filename, message):
        self.filename = filename
        self.message = message
    def __enter__(self):
        with open(self.filename, 'a',encoding='utf-8') as f:
            f.write(f'START: {self.message}\n')
        return self
    def __exit__(self, exc_type, exc_val, traceback):
        with open(self.filename, 'a',encoding='utf-8') as f:
            if exc_type is None:
                f.write(f'END: {self.message}\n')
            else:
                f.write(f'ERROR: {self.message}\n')
        return False
with log_operation('operation.log','Data processing'):
    print('Что то делаем')
try:
    with log_operation('operation.log','Data processing'):
        print('Сейчас будет ошибка')
        raise ValueError('Тестовая ошибка')
except ValueError:
    print('Ошибку поймали снаружи')