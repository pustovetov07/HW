a = input("Введите первое число: ")
what = input("Что делаем? (+, -, *, /, **, //, %):")
b = input("Введите второе число: ")
try:
    a = int(a)
    b = int(b)
    result = a / b
except ValueError:
    print("можно использовать только цифры!!!")

except ZeroDivisionError:
    print("На 0 делить запрещенно!!!")

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
