def converter(string, delimiter):
    res = {}
    words_list = string.split(delimiter)
    for i in set(words_list):
        res.setdefault(i, words_list.count(i))
    return res
string = """a a a b b c a"""
print(converter(string, ' '))