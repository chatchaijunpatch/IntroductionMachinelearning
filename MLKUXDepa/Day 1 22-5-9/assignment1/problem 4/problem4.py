def count_word(i,word):
    count = 0
    for item in word:
        if item == i:
            count+=1
    return count


def count_char(word):
    diction = {}
    word = word.lower()
    for i in word:
        if not i.isalnum():pass
        else:
            diction[i] = count_word(i,word)
    return diction

word = input()
count_char(word)
