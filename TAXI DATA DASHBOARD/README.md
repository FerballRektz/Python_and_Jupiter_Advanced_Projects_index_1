# TAXI DATA DASHBOARD ANALYSIS

## I. Objective
to create a interactive dashboard based on the taxi dataset

## II. Scope
The data used only barplots to visualize the data. There is also  the sorting and ranking of summary statistics of variables.Lastly, The window size might only be compatible in my device as its css and js implementation is not scalable respective to browser size

## III. Data used
The taxi dataset is from the taxi data given to us for making the project the data is obatained from the google cloud big query. The data is consists of more than a million rows that can harbor hardware issures when the whole dataset is used for analysis so a sample of the dataset is taken rather than the whole. 

## IV. How the project is done
The project can consist in these following states:
1. Data Pre-processing
- done in the ipynb script,after obtaining the data, a sample of 100,000 samples is obtained and then cleaned to remove missing values
2. Statistical Analyis
-  done in the ipynb script,total fare amount, average duration, and average milage is used in the dataset to test if there is proven difference between the means of the 3 variables by taxi provider
3. Data Visualisation
- done in the ipynb script,if all the variables has a proven difference of statistical significance , a barplot is then made by averaging the variable by provider
4. Dashboard Making
- using the barplots created in the ipynb script, the code is then integrated to the python script to make a interactive dashboard

## V. Results
The project from the ipynb first shows the scatter plots and statistical test of average total fare amount, average duration, and average milage in which shows there is visual and statistical proof that the average between taxi provider based on the three variables is different.   

Next is the that are created to be integrated in the dashboard, there are three barplots that show averages between providers based on the three criterion.Lastly, is the interactive dashboard. The dashboard has additional interactivity where you can change the barplot color and design.

##  VI. Code and Project Reccomendations
there is both code and project reccomendations that needs to be addressed:  
1. the dashboards design should be more professional 
2. the dashbord should be scalable on its window size to accomodate the dashboard through all the types of devices
3. there should be more research on the dataset to gain more insight for visualisation of the taxi dataset
4. The statistical bootstrapping test should be double checked if it its output is really accurate
5. there should be more practice on html,css,js to improve said dashboard
6. there should be more practice in proper large database management

