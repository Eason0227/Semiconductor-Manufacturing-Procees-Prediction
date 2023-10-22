# Semiconductor-Manufacturing-Procees-Prediction
Dataset from UCI https://archive.ics.uci.edu/ml/datasets/SECOM   
SECOM Dataset: 1567 examples 591 features, 104 fails

## Business Context
A complex modern semiconductor manufacturing process is normally under constant surveillance via the monitoring of signals/variables collected from sensors and or process measurement points. However, not all of these signals are equally valuable in a specific monitoring system. The measured signals contain a combination of useful information, irrelevant information as well as noise. Engineers typically have a much larger number of signals than are actually required. If we consider each type of signal as a feature, then feature selection may be applied to identify the most relevant signals. The Process Engineers may then use these signals to determine key factors contributing to yield excursions downstream in the process. This will enable an increase in process throughput,decreased time to learning and reduce the per unit production costs. These signals can be used as features to predict the yield type. And by analyzing and trying out different combinations of features, essential signals that are impacting the yield type can be identified.

## Objective
We will build a classifier to predict the Pass/Fail yield of a particular process entity and
analyze whether all the features are required to build the model or not.

## Dataset description
Dataset from UCI https://archive.ics.uci.edu/ml/datasets/SECOM 
* The data consists of 1567 examples each with 591 features.
* The dataset presented in this case represents a selection of such features where each example represents a single production entity with associated measured features and the labels represent a simple pass/fail yield for in house line testing.
* Target column “ –1” corresponds to a pass and “1” corresponds to a fail and the data time stamp is for that specific test point

## Data analysis step 
Data preprocessing : 
* Addressing missing value(remove and imputation)
* Examing the data distribution
* Addressing Outliers
* Addressing Multi-collinearity problem (Checking  VIF and correlated independent features)
* Feature selection (XGBoost)
* Normalize data
* Data Oversampling (BoardingLine SMOTE)  

Metric：
* Using Accuracy, Matthews correlation coefficient(MCC), Geometric mean(G-mean), AUC, Sensitivity(Recall), Specificity.
* When dealing with imbalanced datasets, using evaluation metrics such as Sensitivity, MCC (Matthews Correlation Coefficient), and G-means allows for a more comprehensive assessment of the model's performance, especially when focusing on the minority class.

Modeling : 
* Bulid the Logistic regression, KNN, Gradient Boosting Decision Tree, Catboost and XGBoost.
* Using Optuna to tuning the hyperparameter of each model.
* Using ensemble voting method (soft vote ,hard vote) bulid the ensemble model.

## final result 
![image](https://github.com/Eason0227/Semiconductor-Manufacturing-Procees-Prediction/assets/102510341/3d2c7d1b-e17b-4627-ae51-3f861e458ef0)

