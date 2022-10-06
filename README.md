# Semiconductor-Manufacturing-Procees-Prediction
Semiconductor Manufacturing  Prediction  
Dataset from UCI https://archive.ics.uci.edu/ml/datasets/SECOM   
SECOM Dataset: 1567 examples 591 features, 104 fails  

Semiconductor manufacturing processes are often monitored by signals/variables collected from sensors or process measurement points, we treat each type of signal as a feature, apply feature selection to identify the most critical signals, and finally predict based on these features Product success or failure.

## Data analysis step 
Data preprocessing : 
* Addressing missing value(remove and imputation)
* Examing the data distribution
* Addressing Outliers
* Addressing Multi-collinearity problem (Checking  VIF and correlated independent features)
* Feature selection (XGBoost)
* Normalize data
* Data Oversampling (SMOTE)  

Modeling : 
* Bulid the Random Forest, Extra Trees, KNN, Light GBM, Logistic Regression model 
* Using random grid search to tuning the hyperparameter of each model
* Using ensemble voting method (soft vote ,hard vote) bulid the ensemble model
