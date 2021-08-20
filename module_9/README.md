# Predict Baseball Player's Salary Analysis

### Short Description
The aim of this small project is to get familiar with the basics of *ML model deployment* via a micro web framework **Flask** and a cloud PaaS **Heroku**.
I used the [Hitters Baseball Data](https://www.kaggle.com/mathchi/hitters-baseball-data) to train a model, which aim is to predict an annual baseball player's salary using his game performance statistics and years spent in league. For the sake of simplicity and computation speed, I trained simple, easy-to-interpret algorithms for this project. These are Multiple Linear Regression, Decision Tree Regression & k-neighbors Regressor.

### Project Workflow:
* Problem preparation
* Univariate & Multivariate data analysis
* Data cleaning (multicollinearity, missing values, outliers)
* Feature selection (correlation analysis & MI)
* Model selection via 5-fold Cross Validation and MAPE as a measure of prediction accuracy 
* Hyperparameters tuning via GridSearchCV
* Training a final model with the best performing hyperparameters
* Saving the final model with Pickle
* Write a Flask server that accepts a request and process it using our ML-model
* Wrap our server as a cloud service using Heroku

### You can access my salary pediction service by clicking the link below:
#### *https://baseball-player-salary-predict.herokuapp.com/*
