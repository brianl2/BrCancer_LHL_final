# Predicting Malignant or Benign Breast Cancer Tumors Using Supervised Learning and Classical Machine Learning Techniques
This project was done as the Final Project Jan 2022 for the LightHouse Labs Data Science Bootcamp. 


## Introduction & Project Overview
It is estimated that 1 in 8 women in Canada will develop breast cancer in their lifetime. 
As a method of risk prevention and screening, mammography is to visualize if a tumor is present. Breast cancer is often associated with a development of a tumor, which can be either benign (non-cancerous) or malignant (cancerous). 

If the presence of a tumor is found, a biopsy method (like Fine Need Aspiration (FNA)) is the [only definite diagnostic solution](https://cancer.ca/en/cancer-information/cancer-types/breast/diagnosis). The Tumor cell dimensions can be taken from the FNA biopsy and placed into a machine learning model to help identify whether a tumor is likely cancerous or not. 

This implementation of machine learning could help physicians and pathologists in the field by filtering through biopsy results and determining if a given tumor is of concern based on its dimensions. 

## Data
The data for this project can be found here:
Dataset: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

# Project Workflow

## Exploratory Data Analysis: 
Here, we visualize the data and see what we can identify.
  - We find that across all features / measurements of the cells, malignant cancerous cells typically carry higher values (This can be seen in Notebook 1.1 Data Exploration) 
  - However, both benign and malignant cells are highly variable, and thus to reduce the noise of atypical cell sizes, outliers can be removed. 
 
Findings: 
  - There are more benign tumor cells in the Dataset:
![alt text](https://github.com/brianl2/BrCancer_LHL_final/blob/main/data/imbalance.PNG)

  - High multicolinearity between features
  - Data is mostly normal, with few outliers
  - There are no Nulls in this dataset.

## Feature Engineering:
There are many other features that would be interesting to incorporate, such as the presence of family history, the number of normal nucleoli, etc.
However, for this project, I only used the features given by the authors of the dataset, since the measurements given were specific to a given cell. 

Many of the features share colinearity with each other.
  - Features with high colinearity were removed >0.75 correlation 
  - Features were further reduced using the RFE technique 

We were left with 8 features at the end of feature engineering.
These features can be seen at the end of Notebook 1.3 Feature Engineering

## Modeling and Evaluation:
I tested multiple models, with various datasets (Features, new features, and final feature set) 

Here are the results I received from the tests using the final 8 chosen features:
The models were evaluated on multiple metrics, highlighted are the metrics that performed the best.

![alt text](https://github.com/brianl2/BrCancer_LHL_final/blob/main/data/Baseline_models.PNG)

- From this, Logistic regression and SVM performed the best and tried to tune parameters for these two models to improve performance as can be seen in Notebook 2.3 Model Tuning

Ultimately, the default parameters from the SVM model performed the best:

![alt text](https://github.com/brianl2/BrCancer_LHL_final/blob/main/data/best_model.PNG)

## Conclusion:
Machine learning can be used to help reliably identify what tumor cells are malignant and benign, given their measurements from FNA (Fine Needle Aspiration) biopsies. 

As we see with this model, classical machine learning models can classify these tumors very well. However, it is important to note that this dataset is small, and that overfitting could be a huge issue here. We would need a much larger dataset to determine if this model is actually viable. 

Furthermore, the measurements still require humans to do a biopsy and measure the size of these cells, which can be an extensive procedure. The next step for this project would be to use MRI images of breast tumors to identify if the tumors are cancerous or benign. With the proper dataset, computer vision techniques could be used as a helpful tool in breast cancer diagnosis. 

Others have also used computer vision to try and diagnose cancer using MRI images, however the evaluation scores are much less reliable:
https://www.mdpi.com/2076-3417/10/17/6109/pdf

As a final note and some googling:
A dataset for these MRI images was released in April of 2021, the dataset can be found here:
https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=70226903#70226903bcab02c187174a288dbcbf95d26179e8

Perhaps this will be the next project to tackle!

Note: requirements.txt may be incorrect
All required modules are used in Notebook 2.3 Model Tuning, and can be found there. 


