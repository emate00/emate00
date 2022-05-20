#program that reads 10 integers and then finds and prints the sum of the even and odd integers
user_re = 'y'

while user_re == 'y' :

    try:
        print ('Please enter 10 integers:')

        inplist = [] #create empty list

        while len(inplist) < 10:
            inplist.append(int(input('>')))

        #initialize even and odd sum values
        evensum = 0
        oddsum = 0

    # loop sum even digits in inplist
        for i in inplist :
            if i % 2 == 0:
                evensum += i
    # loop sum odd digits in inplist
        for i in inplist :
            if i % 2 != 0:
                oddsum += i

        print ('\nEven sum:', evensum)
        print('Odd sum:', oddsum)

            #exception : print message to user and close program
    except:
        print('User input must be integer. \nPlease restart program.')
        quit()

    repeat = input('\nDo you wish to repeat this program? (y/n)\n>')

    user_re = repeat.lower()

    if user_re == 'n' :
        print('\nDone!')
        quit()

    elif user_re != 'y' :
        print ("Input must be  'y' or 'n'. Please restart.")
        quit()
