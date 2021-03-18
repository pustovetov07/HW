password: str = input("Введите пароль: ")
counter = 0
while True:
    if len(password) <= 8:
        print("Пароль слишком короткий!")
        counter += 1
        password = input()
    elif "123" in password:
        print("слишком просто, попробуй еще раз!!!")
        counter += 1
        password = input()
    else:
        print("Отлично!!")
        print(f"Отгадал пароль за {counter} попыток")
        break





