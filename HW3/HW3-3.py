email: str = input('Введите Email: ') #Придумать емайл
if '@' not in email:
    raise ValueError("Неверный формат почты!!!")
elif '.' not in email:
    raise TypeError("Неверный формат почты!!!")
at_sign_index = email.index('@')
for sign in {'.', '@'}:
    if email[at_sign_index + 1] == sign or email[at_sign_index - 1] == sign:
        raise IndexError("Неверный формат почты!!!")
    elif email[-1] == sign or email[0] == sign:
        raise TypeError("Неверный формат почты!!!")

password: str = input('Введите пароль: ') #придумать пароль
counter = 0
while True:
    if len(password) <= 8:
        raise KeyError("Пароль слишком короткий!!!")
    elif "123" in password:
        raise KeyError("Пароль слишком простой!!!")
    print("Добро пожаловать!!!")
    break