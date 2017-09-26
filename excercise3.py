word1 = input('Enter a word: \n')
word2 = input('Enter a second word: \n')

if len(word1) > len(word2):
    difference = len(word1) - len(word2)
    print('word 1 is longer than word 2 by',difference)
else:
    difference = len(word2) - len(word1)
    print('word 2 is longer than word 1 by',difference)