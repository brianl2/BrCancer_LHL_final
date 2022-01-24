# Predicting Malignant or Benign Breast Cancer Tumors.
This project was done as the Final Project Jan 2022 for the LightHouse Labs Data Science Bootcamp. 

## Introduction and Motive 
It is estimated that 1 in 8 women in Canada will develop breast cancer in their lifetime. 
As a method of risk prevention and screening is to use mammography to visualize if a tumor is present. Breast cancer is often associated with a development of a tumor, which can be either benign (non-cancerous) or malignant (cancerous). With a biopsy, the dimensions of these tumor cells can be used in a machine learning model to help identify whether a tumor is likely cancerous or not. 

This implementation of machine learning could help physicians and pathologists in the field by filtering through mammogram results and determining if a given tumor is of concern based on its dimensions. 

The data for this project can be found here:
Dataset: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29

## Exploratory Data Analysis: 
Here, we visualize the data and see what we can identify from the data. 
  - We find that across all features / measurements of the cells, malignant cancerous cells typically carry higher values. 
  - However, both benign and malignant cells are highly variable, and thus to reduce the noise of atypical cell sizes, outliers can be removed. 
 
Findings: 
  - High multicolinearity between features
  - Data is mostly normal, with few outliers
  - There are no Nulls in this dataset.

## Feature Engineering:
There are many other features that would be interesting to incorporate, such as the presence of family history, the number of normal nucleoli, etc.
However, for this project, I chose to only use the features given by the authors, since the measurements given were specific to a given cell. 
- These features are of various measurements of cells.

Many of the features share colinearity with each other.
  - Features with high colinearity were removed >0.75 correlation 
  - Features were further reduced using the RFE technique 


We were left with 8 features at the end of feature engineering.

## Modeling and Evaluation:
I tested multiple models, with various datasets (Features, new features, and final feature set) 

Here are the results I received from the tests using the final 8 chosen features:


- From this, I determined that Logistic regression and SVM performed the best and tried to tune parameters for these two models to improve performance:

Ultimately, the default parameters from the SVM model performed the best. 

## Conclusion:
Machine learning can be used to help identify what tumor cells are malignant and benign, given their measurements from FNA (Fine Needle Aspiration) biopsies. 

As we see with this model, classical machine learning models can classify these tumors very well. However, it is important to note that this dataset is small, and that overfitting could be a huge issue here. We would need a much larger dataset to determine if this model is actually viable. 

Furthermore, the measurements still require humans to do a biopsy and measure the size of these cells, which can be an extensive procedure. The next step for this project would be to use MRI images of breast tumors to identify if the tumors are cancerous or benign. With the proper dataset, computer vision techniques could be used as a helpful tool in breast cancer diagnosis. 





