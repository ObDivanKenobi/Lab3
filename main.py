# Создать декоратор, который проверяет, что возвращаемое функцией число - целое. Если нет, то оно округляется до сотых.
import decorator
@decorator.a_decorator_rounding_float
def example(x, y):
    return x / y

print("Введите число: ")
x = int(input())
print("Введите еще число: ")
y = int(input())
r = example(x, y)
print("Результат: ", r, ".")