# Калькулятор

from colorama import init
from colorama import Fore, Back, Style

init()

print(Back.BLUE)
print(Fore.BLACK)
print(Style.BRIGHT)
a = float(input("Введите первое число: "))
what = input("Что делаем? (+, -, *, /, **, //, %):")
b = float(input("Введите второе число: "))

if what == "+":
    c = a + b
    print("Результат:" + str(c))
elif what == "-":
    c = a - b
    print("Результат:" + str(c))
elif what == "*":
    c = a * b
    print("Результат:" + str(c))
elif what == "/":
    c = a / b
    print("Результат:" + str(c))
elif what == "**":
    c = a ** b
    print("Результат:" + str(c))
elif what == "//":
    c = a // b
    print("Результат:" + str(c))
elif what == "%":
    c = a % b
    print("Результат:" + str(c))

else:
    print("Выбрана неверная операция!!!")