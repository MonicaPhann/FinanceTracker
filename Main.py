import datetime
#Menu
menu = True
while menu:
    print("Welcome to the Budget Tracker! Select one of the options to get started!")
    while True:
        try:
            user = int(input("1: Add new Transaction \n2: View Transactions\n3: Remove Transactions\n4: Exit\n"))
            break
        except (ValueError):
            print("This is not a valid value please try again!")

    #Add Transaction option
    if user == 1:
        while True:
            try:
                #Inputs the date of transaction
                Year_input = int(input("Input the Year of your transaction (YYYY):\n"))
                Month_input = int(input("Input the Month of your transaction EX: March = '3':\n"))
                Day_input = int(input("Input the Day of your transaction:\n"))
                Date_User = datetime.datetime(Year_input,Month_input,Day_input)

                #Input category and amount of transaction
                Category_User = str(input("Input a Category for you transaction:\n")).capitalize() #Categorys: Food, Clothing, Travel, Other; Create list of new categories?
                Amount_User = float(input("Input an Amount for your transaction:\n"))
                break
            except (TypeError,ValueError):
                print("Oops! This was not a valid value please try again!")

        #Adding new transactions into Transaction file
        openFile = open("Transactions.csv", "a")
        openFile.write(Date_User.strftime("%x") + ',' + Category_User + ',' + str(Amount_User) + '\n')
        openFile.close()
    
    #View Transactions
    if user == 2:
        readFile = open("Transactions.csv", "r")
        for line in readFile:
            data = line.rstrip("\n").split(",")
            print(data)

            #for item in data:
                #print(item)

    #Remove Transactions (Work in progress)
    if user == 3:
        print("This option is still a work in progress!")
    '''
    if user == 3:
        readFile1 = open("Transactions.csv", "r")
        user1 = input("1: Remove specific Transaction\n2: Remove ALL Transactions\n")

        if user1 == 1:
            transactionNumber = int(input("Input transaction number:\n"))
            
            count = 0
            for line in readFile1:
                count += 1
                if transactionNumber == count:
                    print(line)
            
        
        if user1 == 2:
            print(2)
    
    '''
    if user == 4:
        menu = False
            
                
