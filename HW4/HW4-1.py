with open('HW4.txt') as file:
    print(file.read())

with open('HW4.txt') as file_read, open('HW4-1.txt', 'w') as file_write:
    file_write.write(file_read.read())

with open('HW4.txt', 'r+') as file:
    data = file.read()
    file.write('|'.join(data.split('!')))


with open('HW4.txt') as file_read, open('HW4-1.txt', 'w') as file_write:
    file_write.write(file_read.read())
