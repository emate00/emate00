
#create/fill empty list
#intial values; '*' unknown # of args from listSize
def createList(listSize):
    return [0]*listSize

#accepts listSize and return from createList(), fills the passed list (previously 0s)
def fillList (listSize, timeList):
    #for char in range of listSize, set index of char to i
    for i in range(listSize):
        timeList[i] = i
    #void function
    return

#collect call start time (in 24hr notation); return start startHour & startMinute
def collectUserInputTime():
    callstart = None

    while callstart == None:
        callstart = input('Enter the time the call starts in 24-hour rotation:\n')

        if ':' not in callstart:
            print("\nInvalid time entry. Time must contain ':'. \nPlease try again.\n")
            callstart = None
            continue
        ##split input into two variables; split char is ':'
        startHour , startMinute  = callstart.split(':')
        #verify entires are numbers
        try:
            validateHour = int(startHour)
            validateMinute = int(startMinute)
        except:
            print ("\nInvalid time input. Enter time in numerical 24-hour format '00:00'.\nPlease try again.\n")
            callstart = None
    return  startHour , startMinute   #as string values

#collect output from collect collectUserInputTime, validates time within defined 24hr range
#integer has been validated previously
def validateUserInputTime (startHour, startMinute):
    #compare hoursList & minutesList #convert  to integer values
    if int(startHour) in hoursList and int(startMinute) in minutesList:
        #returns True if integer  input is valid
        return True, int(startHour), int(startMinute)
    else:
        #returns False if input is Invalid
        return False

def collectUserInputDay ():
    inputDay = None

    while inputDay == None:
        #collect day input from user
        inputDay = input ('Enter the first two letters of the day of the week:\n')
        #input validation variable
        dayInputValidation = inputDay.lower()
        #verfies that entry is in list, prompts user for correction if entry is invalid
        if dayInputValidation not in daysList:
            print('\nInvalid day input.\nPlease try again.\n')
            inputDay = None
            continue
        else:
            break

    #assigns first and second input character to respective variables (in lower casing for case)
    firstDayCharacter, secondDayCharacter  = inputDay.lower()[0], inputDay.lower()[1]
    return firstDayCharacter, secondDayCharacter

def validateUserInputDay (firstDayCharacter, secondDayCharacter) :
    #concatenate to form date, check against content of daysList
    if (firstDayCharacter + secondDayCharacter) in daysList:
        return True
    else:
        return False

def collectUserInputCallLength () :
    callLength = None

    while callLength == None:
        callLength  = input ('Enter the length of the call in (hours:minutes):\n')
        try:
            callLengthHour, callLengthMinute = callLength.split(":",1)

            #verify entires are numbers

            validatelengthHour = int(callLengthHour)
            validatelengthMinute = int(callLengthMinute)

        except:
            print ("\nInvalid call length input. Entry may contain only numeric values and ':'.\nPlease try again.\n")
            callLength = None
            continue
        return callLengthHour, callLengthMinute

def validateUserInputCallLength (callLengthHour, callLengthMinute):
    if int(callLengthHour) >= 0 and int(callLengthMinute)>= 0 :
        return True, int(callLengthHour), int(callLengthMinute)
    else:
        return False

def calculateTotalCost (startHour, startMinute, firstDayCharacter, secondDayCharacter,callLengthHour,callLengthMinute):
    #calulcate the total cost of a callLenMinutes
    callLengthHour1 = int(callLengthHour)
    callLengthMinute1 = int(callLengthMinute)
    startHour1 = int(startHour)

    if startHour1 >= 8 and startHour1 < 18 :
        rate = 0.40
    elif startHour1 < 8 or startHour1 >= 18:
        rate = 0.25

    if (firstDayCharacter+secondDayCharacter) == 'sa' or (firstDayCharacter+secondDayCharacter) == 'su':
        rate = 0.15

    cost = rate * (callLengthHour1*60 + callLengthMinute1)
    return cost

def collectUserInputYesNo ():
    collectYesNo = None
    while collectYesNo == None:
        collectYesNo = input ('Do you want to repeat the program (y/n)\n')
        YesOrNo  = collectYesNo.lower()
        if YesOrNo in responseList:
            break
        else:
            print('\nInvalid Input.\nPlease try again.\n')
            collectYesNo = None
            continue
    return YesOrNo

#accepts a single arg from collectUserInputYesNo
def validateUserInputYesNo (YesOrNo)  :
    if YesOrNo.lower() in responseList:      #.lower() not required, output from collectUserInputYesNo is lowercase
        return True
    else:
        return False

def clearPreviousOutput(YesOrNo) :
    if YesOrNo.lower() == 'y':
        return True
    else:
        return False

daysList = ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su']
responseList = ['y', 'n']

hoursList = createList(24)
fillList (24, hoursList)
minutesList = createList(60)
fillList(60,minutesList)

YesOrNo = 'y'

while(clearPreviousOutput(YesOrNo)):
    #call prompt user for time input
    startHour, startMinute = collectUserInputTime()


    #while loop to catch erroneous inputs that are not protected for within fx's
    while(not validateUserInputTime(startHour,startMinute)):
        print ('\nInvalid time input. \nPlease try again.\n')
        startHour, startMinute = collectUserInputTime()

    #call prompt for user day input
    firstDayCharacter, secondDayCharacter = collectUserInputDay()
    #call fx to validate day input, passes variables thorugh validation and returns true or false
    while(not validateUserInputDay(firstDayCharacter,secondDayCharacter)):
        print ('\nInvalid day input. \nPlease try again.\n')
        firstDayCharacter, secondDayCharacter = collectUserInputDay()

    callLengthHour, callLengthMinute = collectUserInputCallLength()
    while(not validateUserInputCallLength(callLengthHour,callLengthMinute)):
        print ('\nInvalid call length input. \nPlease try again.\n')
        callLengthHour, callLengthMinute = collectUserInputCallLength()


    #calc cost
    cost = calculateTotalCost(startHour,startMinute, firstDayCharacter,secondDayCharacter,callLengthHour, callLengthMinute)
    #print cost value formatted to 2 decimals; str.format()
    print(cost)
    print("\nCost of the call: ${:.2f} \n".format(cost))

    YesOrNo = collectUserInputYesNo()
    while (not validateUserInputYesNo(YesOrNo)) :
        print('\nInvalid y or n entry.\nPlease try again\n.')
        YesOrNo = collectUserInputYesNo()
