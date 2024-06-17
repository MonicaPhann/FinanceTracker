import datetime
#Menu
print("Welcome to the Budget Tracker!")

Year_input = int(input("Input the Year of your transaction (YYYY): "))
Month_input = int(input("Input the Month of your transaction EX: March = ' 3': "))
Day_input = int(input("Input the Day of your transaction: "))
Date_User = datetime.datetime(Year_input,Month_input,Day_input)



Category_User = str(input("Input a Category for you transaction: ")) #Categorys: Food, Clothing, Travel, Other; Create list of new categories?
Amount_User = float(input("Input an Amount for your transaction (0.00): "))


#Adding new transactions into Transaction file
openFile = open("Transactions.csv", "a")
openFile.write(Date_User.strftime("%x") + ',' + Category_User + ',' + str(Amount_User) + '\n')
openFile.close()
