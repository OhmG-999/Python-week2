# create variables to hold the user input
myword1 = input('Enter the first word: \n')
myword2 = input('Enter the second word: \n')
reversedword = myword1[::-1]


if reversedword == myword2:
    print(myword1,'is the inverse of',myword2)
else:
    print(myword2,'is not the inverse of', myword1)
