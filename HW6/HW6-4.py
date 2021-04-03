def parse(instructions):
    initial_number = 0
    result = []
    res = []
    for operation in instructions:
        if operation == 'i':
            initial_number += 1
        elif operation == 'd':
            initial_number -= 1
        elif operation == 's':
            initial_number **= 2
        elif operation == 'o':
            res.append(initial_number)
    return result
assert parse("iiisdoso") == [8, 64]
