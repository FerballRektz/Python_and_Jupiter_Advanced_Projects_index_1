# WIDSM prediction identificayion using Random Forest Algorithm
In collaboration with:
- TROJAN PATREUS FERRERAS
- AARON JOSHUA BLASURCA


## I. Objective
Is to use machine learning algorithms to identify a persons action in the WIDSM dataset

## II. Scope
The dataset only used the first 5 actions in the WIDSM dataset for easier training of the machine learning model for identifying actions. The machine learning algorithm used in this project is the Random Forest algorithm. 

## III. Data used
The data is obtained from the [WISDM: WIreless Sensor Data Mining](https://www.cis.fordham.edu/wisdm/dataset.php) website. The data is converted into a .csv file from a .txt file for better data pre-process

## IV. How the project is done
The project can be explained in these steps:  
1. Data Pre-processing
- the data is gathered and then cleaned for any possible missing values
2. Feature Engineering
- to find the possible appications and insights that can be obtained from the variables
3. Data Storytelling
-  after finding what insights to find from feature engineering is to create plots for visualisation to help build the machine learning model
4. Machine Model Creation and Evaluation
- the machine learning model is first built using variables deemed important from feature engineering and data storytelling and improving the machine learning model
5. Improving the model
- the machine learning model is improved to increase its accuracy, to increase its accuracy it used a [gradient boosting model](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMClassifier.html) to ensemble with the Random Forest mdodel

## V. Results
The first result obtained from the machine learning model shows the accuracy of the model, here is the output from the Random Forrest:


    Accuracy: 0.5766072738730741

    Classification Report:
                precision    recall  f1-score   support

        jogging       0.59      0.59      0.59    172423
        sitting       0.75      0.74      0.74    175316
        stairs        0.40      0.43      0.41    168120
        standing      0.66      0.74      0.70    176119
        walking       0.47      0.38      0.42    177600

        accuracy                          0.58    869578
        macro avg     0.57      0.58      0.57    869578
        weighted avg  0.57      0.58      0.57    869578

Based from the first output, it is shown that the accuracy of the model is 57% which is above average for a human action identification model. Based from the precision of the actions there are 2 actions that is under 50% which is walking and stairs

The improved machine learning model using gradient boosting results:

    Accuracy: 0.6406314327179391

    Classification Report:
                precision    recall  f1-score   support

    jogging       0.64      0.63      0.64    172423
    sitting       0.83      0.79      0.81    175316
    stairs        0.46      0.46      0.46    168120
    standing      0.76      0.81      0.78    176119
    walking       0.50      0.51      0.51    177600

    accuracy                          0.64    869578
    macro avg     0.64      0.64      0.64    869578
    weighted avg  0.64      0.64      0.64    869578

The improved machine learning model shows a 10% increase in its accuracy and a improvement on the precision of each action. Based from the precision of the actions in the improved model there is now only 1 action that is under 50% which is stairs

##  VI. Code and Project Reccomendations
there is both code and project reccomendations that needs to be addressed:  
1. Use other machine learning model to improve the model(preferrable a ANN model)
2. Extend the actions that the model needs to learn
3. Increase knowledge on other types of machine learning models and methematics to understand how machine learning model works
4. Increase knowledge in other python libaries to possibly find more optimal models
5.  Increase knowledge in python to make code more professional and more easier to read and debug 




