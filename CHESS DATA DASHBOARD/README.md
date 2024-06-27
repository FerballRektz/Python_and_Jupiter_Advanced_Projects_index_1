# CHEST DATA ANALYSIS AND DASHBOARD 

## I. Objective
to create a interactive visualisation on vital information about a chest player in the chest data set
## II. Scope
the visualisations will be interactive types with no statistical test needed, I do not know where the dataset is also obtained which makes the columns in the dataset up to the interpretation of the one using the data, the dataset also contains missing infotrmation that may miss vital insights and visualisation. The window size might only be compatible in my device as its css and js implementation is not scalable respective to browser size
## III. Data used
the variables that is used in the data is the ff(this is my interpretation):
- id = string, ID for match 

- rated =  bool, checks if the match is rated or not

- variant = string, speed of the chest match 

- speed = string, checks if the match is classical or rapid type

- perf = string, the chest players performance 

- createdAt = int, checks what time the match started

- lastMoveAt = int, checks what time the match finished

- status = sting,outcome of the chest match

- players =  dictionary, a python dictionary containing player and enemy information

- opening = dictionary, a python dictionary containing information about the opening move of the match

- moves = string, shows the chestmoves in the match

- clock = dictionary, a python dictionary on the time data of the match

- winner = string, chest color that won 

- analysis = dictionary, a python dictionary on analysis of moves

- tournament = no information

## IV. How the Project is done
the project is done first on ipynb and on py, these two scripts ecompass the ff:<br>
1. Data Cleaning and Data Visualisation
- this script is made in ipynb file, it shows how the raw chest data is pre-processed then used to create experimental  interactive graphs for the creation of the interactive dashboard
2. Creation of Dashboard
- the script is made in a py file, it shows the expiremented graphs that is in the ipynb file that is now integrated in the interactive dashboard

## V. Results
the final output this project shows is a interactive dashboard that shows the data of each player from what is thier favorite opening, thier win ratio, elo, and many more. the interactive dashboard can be used to explain if the chest player is effective or not

##  VI. Code and Project Reccomendations
there is both code and project reccomendations that needs to be addressed:
1. the dashboards design should be more colorful and pleasing to the eye
2. the dashbord should be scalable on its window size to accomodate the dashboard through all the types of devices
3. there should be more research and code experimentation on interactive graphs that can show chest player statistics for more effectively 
4. the dataset used should be gathered in more reliable with no missing columns and explainable documentation on its column name and data
5. there should be more practice on html,css,js to improve said dashboard






