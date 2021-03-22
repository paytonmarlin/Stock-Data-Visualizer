#File created 10 March 2021
#*****PLEASE READ******
# the input function only works in CLI with python3 
#***************************************



#Could have a function that checks for user input (no letters, negatives, etc.)
#Putting it all in a loop to ask for user input

import datetime
import requests
import calendar
#function to check times
def date_Format_Check(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
#make sure there is no future dates or the current date
def no_Future_Dates(date):
    today = datetime.datetime.now()
    if date > today:
        return False
    elif date == today:
        return False
    else:
        return True

#make sure dates are not past 19 years
def nothing_Past_19(year, month):
    today = datetime.datetime.now()
    in_past_year = today.year - 19
    in_past_month = today.month
    
    if year < in_past_year:
        
        if month < in_past_month:
            
            return False
        else:
            
            return True

    
while(True):
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
        stock_symbol = input("Please choose a stock symbol to visualize  \n>>>: ")
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
            chart_Choice = float(input("Please choose a chart type /n>>>: "))
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
            time_seriesDict = { 1: 'TIME_SERIES_INTRADAY', 2: 'TIME_SERIES_DAILY', 3: 'TIME_SERIES_WEEKLY', 4: 'TIME_SERIES_MONTHLY'}
            time_Choice = int(input("Please enter the time of the stock data>>>: "))
            time_series = time_seriesDict[time_Choice]
            if time_Choice <= 0:
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print("That's not a choice please enter a number in the range of 1-4")
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
                print(time_series[time_Choice])
            else:
                if time_Choice > 4:
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print("That's not a choice please enter a number in the range of 1-4")
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
                    print(time_series[time_Choice])
                else:
                    check_time += 1
        except:
            print("*-*-*-*-*-*-*-*-*-*-*")
            print("That's not a number please choose a number")
            print("*-*-*-*-*-*-*-*-*-*-*\n")
            print(time_series[time_Choice])



#Enter the beginning Date (YYYY-MM-DD)
    check_Bdate = 0
    while check_Bdate < 1:
        print("""
            Enter the Beginning Date
            ---------------------------------------------------------
            """)
        date_B_Choice = input("(YYYY-MM-DD) >>>: ")
        format_Answer = date_Format_Check(date_B_Choice)
        if format_Answer == False:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        else:
            begin_List = date_B_Choice.split("-")
            begin = datetime.datetime(int(begin_List[0]), int(begin_List[1]), int(begin_List[2]))
            in_Future = no_Future_Dates(begin)

            if in_Future == False:
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print("This date is in the future please enter a date in the past")
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
            else:
                
                in_past = nothing_Past_19(begin.year, begin.month)
                if in_past == False:
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print("This date is in too far in the past")
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
        date_E_Choice = input("(YYYY-MM-DD) >>>: ")
        format_Answer = date_Format_Check(date_E_Choice)
        if format_Answer == False:
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
            print("This is the incorrect date string format. It should be YYYY-MM-DD")
            print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
        else:
            #this checks to make sure that the end date is not before the beginning date
            
            end_List = date_E_Choice.split("-")
            
             
            end = datetime.datetime(int(end_List[0]), int(end_List[1]), int(end_List[2]))
            in_Future = no_Future_Dates(end)
            if begin < end:
                if in_Future == False:
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                    print("This date is in the future please enter a date in the past")
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
                else:
                    in_past = nothing_Past_19(end.year, end.month)
                    if in_past == False:
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                        print("This date is in too far in the past")
                        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
                    else:
                        check_Edate += 1
            else:
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print("This is the incorrect End date can not be before Beginning date")
                print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")

    #Builds the URL string to get the JSON data from AlphaVantage
    api_key = 'GR8VROXU8ASO7XHX'
    base_url = 'https://www.alphavantage.co/query?'
    params = { 'function': time_series,
                'symbol': stock_symbol,
                'interval': '30min',
                'outputsize': 'full',
                'apikey': api_key}
    
    response = requests.get(base_url, params=params)
    #print(response.json())
    #print(str(response.json()))
    if "Error Message" in response.json() :
        print("The server is either down or you provided a ticker symbol that does not exist")
      
    else:
        #print(response.json())

        #test to print URL
        url = 'https://www.alphavantage.co/query?function=' + time_series + '&symbol=' + stock_symbol + '&interval=' + '30min' + '&apikey=' + api_key
        print(url)
        #JSON Will be conqured
        json_time_seriesDict = { 1: 'Time Series (30min)', 2: 'Time Series (Daily)', 3: 'Weekly Time Series', 4: 'Monthly Time Series'}
        json_response = response.json()
        time_json_object = json_time_seriesDict[time_Choice]
    
        #print(json_response[time_json_object])

        #call function to generate date range
        #date_range = date_Interval_Calculator(time_Choice, begin, end)
        #for dates in date_range:
           # try:
             #   print(dates)
             #   print(json_response[time_json_object][dates])
            #except:
             #   print("The date you enter does not exist in this data")

        for date_key in json_response[time_json_object]:
            if time_Choice == 1:
                real_date_key = datetime.datetime.strptime(date_key,"%Y-%m-%d %H:%M:%S")
            else:
                real_date_key = datetime.datetime.strptime(date_key,"%Y-%m-%d")
            
            if real_date_key >= begin and real_date_key <= end:
                print(date_key)
                
                json_open = []
                json_open.append(json_response[time_json_object][date_key]["1. open"])
                
                json_high = []
                json_high.append(json_response[time_json_object][date_key]["2. high"])
                
                json_low = []
                json_low.append(json_response[time_json_object][date_key]["3. low"])
                
                json_close = []
                json_close.append(json_response[time_json_object][date_key]["4. close"])
                

                
#Chart will then open in new browser
   

    #checks at the end if they want to visulize again
    y = input("\n \n Would you like to calculate again? \n\n YES, y \n\n NO, n \n>>>:")
    if (y != "y"):
        break
        











    

