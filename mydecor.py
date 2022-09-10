class Tracer:
    def __init__(self, func): # Запоминает исходный начальный счётчик
        self.calls = 0
        self.func = func
    def __call__(self, *args): # При последующих вызовах: добавляет логику, запускает оригинал
        self.calls += 1
        print(f"call {self.calls}, {self.func.__name__}")
        return self.func(*args)
@Tracer
def spam(a, b, c): # Помещает spam внутрь объекта декоратора
    return a + b + c
print(spam(1, 2, 3)) # На самом деле обращается к объекту-оболочке Tracer
print(spam("a", "b", "c")) # Вызывается метод __call__ из класса
#spam(1, 2, 3)
#spam("a", "b", "c")
# ZART FROM PYTHON BEGGINERS
"""
##### декоратор ##########

class Tracer:
    def init(self, func): # Запоминает исходный начальный счётчик
        self.calls = 0
        self.func = func
    def call(self, *args): # При последующих вызовах: добавляет логику, запускает оригинал
        self.calls += 1
        print(f"call {self.calls}, {self.func.name}")
        return self.func(*args)

##### декоратор закончился ##########

##### далее пример использования декоратора ##########

@Tracer
def spam(a, b, c): # Помещает spam внутрь объекта декоратора
    return a + b + c

print(spam(1, 2, 3)) # На самом деле обращается к объекту-оболочке Tracer
print(spam("a", "b", "c")) # Вызывается метод call из класса
"""
