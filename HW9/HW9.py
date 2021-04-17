import string
import random
import zipfile

PASSWORD_LENGTH = 4

def extract_archive(file_to_open, password):
    try:
        file_to_open.extractall(pwd=password.encode())
        return True
    except Exception as e:
        print(e)
        return False

def build_pass():
    empty = ''
    for _ in range(PASSWORD_LENGTH):
        empty += random.choice(string.digits)
    return empty

def hack_archive(file_name):

    file_to_open = zipfile.ZipFile(file_name)
    wrong_passwords = set()
    tries = 0

    while True:

        password = build_pass()

        if password in wrong_passwords:
            continue
        elif extract_archive(file_to_open, password):
            break
        wrong_passwords.add(password)
        tries += 1

    print(f'Archive {file_name} is hacked. Password - {password}')
    print(f'Password was found after {tries} tries')

filename = 'task.zip'
hack_archive(filename)