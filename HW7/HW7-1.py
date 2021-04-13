def get_max_num(array):
    int_list = []
    arr = ''.join(map(str, array))
    for i in arr:
        int_list.append(i)
    int_list = sorted(list(map(int, int_list)), reverse=True)
    return int(''.join(map(str, int_list)))
print(get_max_num([61, 228, 9]))
