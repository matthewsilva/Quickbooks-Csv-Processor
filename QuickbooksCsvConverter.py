#!/usr/bin/env python3


# Changes ordering of dates
def reformatDates(dates):
    newDates = []
    for i in range(len(dates)):
        month, day, year = dates[i].split("/")
        newDate = day + "/" + month + "/" + year
        newDates = newDates + [newDate]
    return newDates


# Function to open a file - using exception handling
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("\nEnter name of data file: ")
        # Begin exception handling
        try:
            # Try to open the file using the name given
            dataFile = open(fname, 'r')
            # If the name is valid, set Boolean to true to exit loop
            goodFile = True
        except IOError:
            # If the name is not valid - IOError exception is raised
            print("\nInvalid filename, please try again ... ")
    return dataFile

# Get the quickbooks csv data from a file that the user provides
def getData():
    # Open the data file
    print("\n-----GETTING QUICKBOOKS CSV DATA---------")
    print("\nEnter Quickbooks csv data file name when prompted")
    print("\n(Be sure that the csv is in the same directory as this program)")
    infile = openFile()
 
    # Initialize the empty lists
    checkNums = []
    dates = []
    amounts = []
    payees = []
 
    # Read a line from the file 
    line = infile.readline()
 
    # Loop while the end of file is not reached
    while line != "":
 
        # Strip the \n from the end of the line
        line = line.strip()
 
        # Split the two items in the list separated by a comma
        checkNum, date, amount, payee = line.split(",")
        
        # Add the name to the names list
        checkNums = checkNums + [checkNum]
 
        # Add the grade to the grades list
        dates = dates + [date]

        # Add the grade to the grades list
        amounts = amounts + [amount]

        # Add the grade to the grades list
        payees = payees + [payee]
  
        # Read the next grade from the file
        line = infile.readline()
               
    # Close the file
    infile.close()

    # Fix the date format
    dates = reformatDates(dates)
 
    # Return the names and grades lists
    return checkNums, dates, amounts, payees

def getInfo():
    print("\n-----GETTING YOUR ACCT & ROUTING NUMBERS---------")
    answer = ""
    answer = input('\nSaved data file or manual input? (Please type "save" or "manual"): ')
    while (answer != "save" and answer != "manual"):
        answer = input('\nPlease type "save" or "manual": ')
    if (answer == "manual"):
        acctNum = input("\nPlease enter account number: ")
        routingNum = input("\nPlease enter routing number: ")
        answer = input('\nWant to save account and routing number to file for easy use? (y/n):')
        while(answer != "y" and answer != "n"):
        	answer = input("\nInvalid response, please enter 'y' or 'n'):")
        if (answer == "y"):
        	saveFile = open("Save/save.txt", "w")
        	saveFile.truncate(0)
        	saveFile.write(acctNum + ", " + routingNum + "\n")
        	print("\nData saved!")
        elif (answer == "n"):
        	print("\n'n' selected, data not saved")
    elif (answer == "save"):
        infile = open("Save/save.txt")
        line = infile.readline()
        line = line.strip()
        acctNum, routingNum = line.split(",")
        acctNum = acctNum.strip()
        routingNum = routingNum.strip()
        print("\nData Loaded")
    return acctNum, routingNum

# Outputs the new easypay compatible csv data to a file the user provides
def outputNewCsv(checkNums, dates, amounts, payees):
    acctNum, routingNum = getInfo()
    print("\n-----WRITING NEW CSV TO FILE-----")
    fname = input("\nEnter name of output file: ")
    outFile = open(fname, 'w')
    outFile.write("Account Number, Routing Number, Check Number, Date, Amount, I, Payee \n")
    for i in range(len(checkNums)):
        outFile.write(acctNum + ", " + routingNum + ", " + checkNums[i] + ", " + dates[i] + ", " + amounts[i] + ", " + payees[i] + "\n")

    outFile.close()
    return fname
 
 
# Main Function
def main():
	
    # Get the grades from the file
	checkList, dateList, amountList, payeeList = getData()
 
	fname = outputNewCsv(checkList, dateList, amountList, payeeList)
 
	print("\nEasyPay compatible csv written to data file " + fname)

        
if __name__ == "__main__":
    main()

