# Declare 2 variables to hold each of the user input
rhyme1 = input('Enter your first word: \n')
rhyme2 = input('Enter your second word: \n')


def verifyifstring(word):
    if word.isnumeric():
        print('one of the input contains numeric value(s)\n')
        return True;
    else:
        return False;


def checkifrhyme(word1, word2):
    end1 = word1[-4:]
    end2 = word2[-4:]

    if end1 == end2:
        print('Thumbs up! "',word1,'" and "',word2,'" are making a nice rhyme')
    else:
        print('Well..."',word1,'" and "',word2,'"are not making a rhyme')
        return


myrhyme1 = verifyifstring(rhyme1)
myrhyme2 = verifyifstring(rhyme2)

while myrhyme1 == False and myrhyme2 == False:
    checkifrhyme(rhyme1, rhyme2)

    rhyme1 = input('Enter your first word: \n')
    rhyme2 = input('Enter your second word: \n')



rhyme1 = input('Enter your first word: \n')
rhyme2 = input('Enter your second word: \n')
