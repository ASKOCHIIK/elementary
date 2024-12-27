def func(x, d):
    return x + d

def subtract(x, d):
    return x - d

def multiply(x, d):
    return x * d

def divide(x, d):
    if d != 0:
        return x / d
    else:
        return "bag"

x = 10
d = 5

print("Сложение:", func(x, d))
print("Вычитание:", subtract(x, d))
print("Умножение:", multiply(x, d))
print("Деление:", divide(x, d))
print("Деление на ноль:", divide(x, 0))

