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
| Payton Marlin | Scrum Master |
| Jack Dempsey | Text |
| Noah Kirsch | Text |
| Joe Sahrmann | Text |
| Shawn Nguyen | Text |
| Yang (Scott) Lui | Text |
| Emajin Brown| Text |
---
### Tasks
- [x] Get starting Python Code up
- [x] Coordinate group efforts, split into teams
- [x] Basic User function/error checking - Python Code
- [x] Getting API from Alpha Vantage via the 'requests' library
- [x] Parse data into JSON
- [ ] Use JSON to convert to graphical representation of stock data
---
### Useful Sources:
- [Alpha Vantage](https://www.alphavantage.co/) - Website where an API Key can be generated
- [Learn Python](https://www.learnpython.org/)
- [PyGal](http://www.pygal.org/en/stable/documentation/types/index.html) - Graphing Module for python for easier rendering of charts
- [Lxml](https://lxml.de/) - Allows chart to be rendered in web browser
- [Requests](https://requests.readthedocs.io/en/master/) - Used to make http requests and can query the API

### Meetings
Below is a list of meetings and what the general discussion was about...

**March 9th - Initial Meeting**

-----

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
