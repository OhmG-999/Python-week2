myday=input('Enter a day of the week \n')

dayoftheweek = myday.lower()

def daynumber(day):

    if 'mo' in day[0:2]:
        print(day,'is the 1st day of the week')
    elif 'tu' in day[0:2]:
        print(day,'is the 2nd day of the week')
    elif 'we' in day[0:2]:
        print(day,'is the 3rd day of the week')
    elif 'th' in day[0:2]:
        print(day,'is the 4th day of the week')
    elif 'fr' in day[0:2]:
        print(day,'is the 5th day of the week')
    elif 'sa' in day[0:2]:
        print(day,'is the 6th day of the week')
    elif 'su' in day[0:2]:
        print(day,'is the 7th day of the week')
    else:
        print('this is not a day of the week')


daynumber(dayoftheweek)