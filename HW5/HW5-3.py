def clean_text(text:str):
    scrap = ['.', ',', '?', '!', ':', ';']
    splited_text = text.split(' ')
    for word in splited_text:
        for lit in word:
            if lit in scrap:
                word.replace(lit, '')
    print(splited_text)
    return splited_text

def find_biggest(text:list):
    biggest_word = ''
    for word in text:
        if len(word) > len(biggest_word):
            biggest_word = word

    return  biggest_word

def findCommonword(text:list):
    common_word = ''
    for word in text:
        if text.count(word) > text.count(common_word):
            common_word = text.pop(text.index(word))

    return common_word

def parse(text:str):
    clear_text = clean_text(text)
    biggest_word = find_biggest(clear_text)
    common_word = findCommonword(clear_text)
    return (common_word, biggest_word)

def main():
    text = input()
    print(*parse(text))

if __name__ == '__main__':
    main()
