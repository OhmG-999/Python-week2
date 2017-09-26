# gather user's word
word = input('Enter a 5 character word: \n')

# verify the length of the word
check = len(word)

# if the word is exactly 5 characters then start checking if it is palindrome
while check is 5:

    if word[0] == word[-1] and word[1] == word[-2] and word[2] == word[-3]:
        print(word,'is a palindrome')
    else:
        print(word,'is not a palindrome')
# ask user for new word
    word = input('Enter a 5 character word: \n')
    check = len(word)

# if the word is longer or shorter than 5 characters; or the input contains digital then the program terminate
print('it\'s over')