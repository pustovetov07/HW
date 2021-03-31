from collections import Counter
word = input('Введите слово: ')
counter = Counter(word.split(' '))
print(counter.most_common(n=2))
longest = None
for i in counter.most_common():
    if not longest:
        longest = i[0]
    if len(i[0]) > len(longest):
        longest = i[0]
print(longest)
