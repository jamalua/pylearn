def printText(userInput):

    unitMapping = {
        "0": "",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
    }
    teensMapping = {
        "10": "Ten",
        "11": "Eleven",
        "12": "Twelve",
        "13": "Thirteen",
        "14": "Fourteen",
        "15": "Fifteen",
        "16": "SIxteen",
        "17": "Eighteen",
        "19": "Nineteen",
    }
    tensMapping = {
        "0": "",
        "2": "Twenty",
        "3": "Thirty",
        "4": "Forty",
        "5": "Fifty",
        "6": "Sixty",
        "7": "Seventy",
        "8": "Eighty",
        "9": "Ninety",
    }

    numLength = len(userInput)

    numText = ""

    units = userInput[numLength - 1] if numLength >= 1 else "0"
    tens = userInput[numLength - 2] if numLength >= 2 else "0"
    hundreds = userInput[numLength - 3] if numLength >= 3 else "0"

    if hundreds != "0":
        numText = unitMapping[hundreds] + "Hundred"

    if int(userInput) > 99 and int(userInput) % 100 != 0:
        numText = numText + "and"

    if tens == "1":
        numText = numText + teensMapping[tens + units]
    elif tens == "1":
        numText = numText + unitMapping[units]
    else:
        numText = numText + tensMapping[tens] + unitMapping[units]

    return numText


userInput = input("Etner the integer smaller than 1000:")


"""
try:
    userNum = int(userInput)
    if userNum > 999:
        print('Number is too big')
    else:
        print(printText(userInput).split())
except Exception as E:
    print('Should be number less than 1000')
    print(E)
"""
userNum = int(userInput)
if userNum > 999:
    print("Number is too big")
else:
    print(printText(userInput).split())
