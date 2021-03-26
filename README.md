# Stock-Data-Visualizer
## Some Info...

This is a stock data visualizer for INFOTC 4320 - Software Engineering. This is made using python by getting the API from the [Alpha Vantage](https://www.alphavantage.co/) website.

---------------------------
### Requirements: 
"The application should:

- Ask the user to enter the stock symbol for the company they want data for.
- Ask the user for the chart type they would like.
- Ask the user for the time series function they want the api to use.
- Ask the user for the beginning date in YYYY-MM-DD format.
- Ask the user for the end date in YYYY-MM-DD format.
    -   The end date should not be before the begin date
- Generate a graph and open in the user’s default browser"
----------------------------
### Members:

| Member | Main Role |
| ----------- | ----------- |
| Payton Marlin | Scrum Master - API Team |
| Jack Dempsey | Python Validation |
| Noah Kirsch | Chart Group |
| Joe Sahrmann | Python Validation |
| Shawn Nguyen | API Team |
| Yang (Scott) Lui | Chart Group |
| Emajin Brown| Chart Group |
---
### Tasks
- [x] Get starting Python Code up
- [x] Coordinate group efforts, split into teams
- [x] Basic User function/error checking - Python Code
- [x] Getting API from Alpha Vantage via the 'requests' library
- [x] Parse data into JSON
- [x] Use JSON to convert to graphical representation of stock data

### Some problems found
- [x] How to loop over data and display into new browser
    - Got done with FOR loop and added a list for each of the four data (open, high, close, low)
- [x] How to display data for the INTRADAY function (right now no data is outputted)
    - Figured out it, needed a seperate FOR loop to check the date for the specific day.
---
### Useful Sources:
- [Alpha Vantage](https://www.alphavantage.co/) - Website where an API Key can be generated
- [Learn Python](https://www.learnpython.org/)
- [PyGal](http://www.pygal.org/en/stable/documentation/types/index.html) - Graphing Module for python for easier rendering of charts
- [Lxml](https://lxml.de/) - Allows chart to be rendered in web browser
- [Requests](https://requests.readthedocs.io/en/master/) - Used to make http requests and can query the API

## Walkthrough (Git/Github)
### STEP 1: Clone Repository to local machine!

First, you need to copy the repository to your local machine (computer). **You ONLY need to do this once** 

This command follows the syntax *git clone [repo_url]*...
```
git clone https://github.com/paytonmarlin/Stock-Data-Visualizer.git
```
![Git_Clone](/assets/Git_Clone.gif)

This will put all the repository files, as well as a '.git' folder to keep version control history. 

### STEP 2: Pull the contents of the repo to your local machine (if a change has been made on the github repo)

If there has been a change on the remote repo on Github, you should pull the contents before you try and push your changes. If you push changes when there has been a change remotely (by a different collaborator), git will tell you to pull.

This is why I made this step second, always pull before you start on your portion of the project.

This command follows the syntax...
```
git pull
```
![Git_Pull](/assets/Git_Pull.gif)

### STEP 3: Work in the development branch, THEN merge with your main branch once done

It is wise to work in the development branch (which has already been made), and then merging it with the main once everything works well together. 

*git checkout [branch_name]* switches to the branch to work on. 
**Do this first before the main branch to not complicate merge errors!**

```
git checkout development
~~ do some stuff, commit, push ~~
git checkout main
~~ 
git merge development
```
![Git_Branches](/assets/Git_Branches.gif)


### STEP 4: Commit and Push your changes to the remote repository once you have finished a portion of the project.

Once you have made changes, commit them before pushing them with a message that signals what changes have been made. After commiting, you can push them to the remote repository so everyone can pull your changes. 
 
 - Make sure you pull before you push in case there has been any changes
 - Commit your changes with a useful, short, message
 - I would work on the development branch first, and then merge with the main once you are done to try and consolidate development errors.
 

This follows the syntax, *git commit -a (adds all files to be stages to push) -m (a message) "Your message"*

```
git commit -a -m "This is a commit
~~
git push
```
![Git_PUsh](/assets/Git_Push.gif)

---
## Walkthrough for Data Visualizer
This will be done through the terminal through Visual Studio Code, but can be done through either IDLE or your own terminal/command line/powershell. All you need to do is to navigate to the location in which the *Data_Visualizer.py* file is stored. We will be showing the line graph, since that is our preferred method to read the data, but this data can also be submitted to show a bar graph if that works best for you. 

**Method #1: Getting Stock Data through one day (Intraday)**

The *Intraday* function is unique in that it returns data through one specific day (the beginning of the opening day to the close of the trading day).Due to the large amount of data, we ask that you only get data **in the past three days** if you are choosing Intraday. Technically, the data stored in [AlphaVantage's](https://www.alphavantage.co/documentation/) Intraday function is from the last 60 days, but we wanted to restrict this to only the past three days. See below on how to set up the Intraday function

![Intraday](/assets/Intraday.gif)

**Method #2: Getting Stock Data over multiple days**

The *Daily* function is a great function to see what has happend over the course of a couple days (usually under 30 days, but can be more if you want more detailed data). This function, however, differs from the Intraday function in that it doesn't have a limit to the past couple days. Alpha Vantage stores data from the past ~20 years, so no need to try and find data that is in this year. Let have a look at the daily stock data of TSLA in 2016... 

![Daily](/assets/Daily.gif)

**Method #3: Getting Stock Data over multiple weeks**

The *Weekly* function is useful for getting data over multiple weeks. Sometimes, looking at daily stock graphs won't give as big of a picture as some would like. Let's look at the GME stock in Febuary...

![Weekly](/assets/Weekly.gif)

**Method #4: Getting Stock Data over multiple months**
For the biggest picture to see what happend to a stock over the course of months, the *Monthly* function is used. Let's look at the stock of Microsoft during a few months in 2004

![Monthly](/assets/Monthly.gif)