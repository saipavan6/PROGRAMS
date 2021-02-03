word = input('enter a word')
lenght_word = len(word)
rev_word = ''
while lenght_word >=1:
    rev_word = rev_word + word[lenght_word - 1]
    lenght_word = lenght_word -1
print(rev_word)
if word == rev_word :
    print('palindrome')
else :
    print('not')
