#File created 10 March 2021
#*****PLEASE READ******
# the input function when dealing with characters does not work in CLI
# you must use raw_input instead
# if you are testing in IDLE use input
# if you are testing in CLI use raw_input
#***************************************



#Could have a function that checks for user input (no letters, negatives, etc.)
#Putting it all in a loop to ask for user input

import datetime
#function to check times
def date_Format_Check(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False    


y = "y"
while y == 'y':
    #create varibles to hold user input
    stock_symbol = ""
    chart_Choice = 0
    time_Choice = 0
    date_B_Choice = ""
    date_E_Choice = ""

#Another function could check the end date against beginning date


#This could be the main program

    #User enters stock symbol, may need to be validated
    print("""
        Stock Data-Visualizer
    -----------------------------\n""")
    check_stocks = 0
    while check_stocks < 1:
        stock_symbol = raw_input("Please choose a stock symbol to visualize  \n>>>:")
        if len(stock_symbol) < 1 or len(stock_symbol) > 5 :
            check_stocks = 0
            print("*-*-*-*-*-*-*-*-*-*-*")
            print("That's not a stock symbol")
            print("*-*-*-*-*-*-*-*-*-*-*\n")
        else:
            if any(map(str.isdigit, stock_symbol)):
                print("*-*-*-*-*-*-*-*-*-*-*")
                print("That's not a stock symbol")
                print("*-*-*-*-*-*-*-*-*-*-*\n")
            else:
                #do a check here to make sure if it is a real stock or not
                check_stocks += 1
            
    #User enters the chart type wanted (either bar or line)
    check_chart = 0
    while check_chart < 1:
        try:
            print("""
            Chart Types
            -------------------
            1. Bar
            2. Line
            """)
            chart_Choice = float(input(">>>: "))
            if chart_Choice <= 0:
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print("That's not a choice please enter either 1 or 2")
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
            else:
                if chart_Choice > 2:
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print("That's not a choice please enter either 1 or 2")
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
                else:
                    check_chart += 1
        except:
            print("*-*-*-*-*-*-*-*-*-*-*")
            print("That's not a number please choose a number")
            print("*-*-*-*-*-*-*-*-*-*-*\n")    



    #User inputs the time series wanted between the four options
    check_time = 0
    while check_time < 1:
        try:
            print("""
            Select the Time Series of the chart you want to Generate
            ---------------------------------------------------------
            1. Intraday
            2. Daily
            3. Weekly
            4. Monthly
            """)
            time_Choice = float(input(">>>: "))
            if time_Choice <= 0:
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print("That's not a choice please enter a number in the range of 1-4")
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
            else:
                if time_Choice > 4:
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print("That's not a choice please enter a number in the range of 1-4")
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
                else:
                    check_time += 1
        except:
            print("*-*-*-*-*-*-*-*-*-*-*")
            print("That's not a number please choose a number")
            print("*-*-*-*-*-*-*-*-*-*-*\n")    



#Enter the beginning Date (YYYY-MM-DD)
    check_Bdate = 0
    while check_Bdate < 1:
        print("""
            Enter the Beginning Date
            ---------------------------------------------------------
            """)
        date_B_Choice = raw_input("(YYYY-MM-DD) >>>: ")
        format_Answer = date_Format_Check(date_B_Choice)
        if format_Answer == False:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        else:
            check_Bdate += 1
            
 
#Enter the end Date (YYYY-MM-DD)
    check_Edate = 0
    while check_Edate < 1:
        print("""
            Enter the End Date
            ---------------------------------------------------------
            """)
        date_E_Choice = raw_input("(YYYY-MM-DD) >>>: ")
        format_Answer = date_Format_Check(date_E_Choice)
        if format_Answer == False:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        else:
            #this checks to make sure that the end date is not before the beginning date
            begin_List = date_B_Choice.split("-")
            end_List = date_E_Choice.split("-")
            
            begin = datetime.datetime(int(begin_List[0]), int(begin_List[1]), int(begin_List[2])) 
            end = datetime.datetime(int(end_List[0]), int(end_List[1]), int(end_List[2]))

            if begin < end:
                check_Edate += 1
            else:
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print("This is the incorrect End date can not be before Beginning date")
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

#Chart will then open in new browser
            
    #checks at the end if they want to visulize again
    y = raw_input("\n \n Would you like to calculate again? \n\n YES, y \n\n NO, n \n>>>:")
        
#Good-bye message if they don't choose y
if y!= 'y':
    print("*")
    print("*~*")
    print("*~*~*")
    print("*~*~*~*")
    print("Good Bye :)")
    print("*~*~*~*")
    print("*~*~*")
    print("*~*")
    print("*")











    

