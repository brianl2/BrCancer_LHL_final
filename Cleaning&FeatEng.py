# Function for Data Cleaning and Feature Engineering -> For Direct modeling. 
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np 

def cleaning_features(df):
    '''Cleans a given dataframe of breast cancer metrics, to be used in the model.
    Input: Dataframe 
    Output: X_train, X_test, y_train, y_test'''
    sm = SMOTE(random_state=42)
    finallist = ['diagnosis','radius_mean', 'texture_mean','symmetry_mean','fractal_dimension_mean','radius_se','smoothness_se', 'symmetry_se', 'symmetry_worst']
    print('Cleaning Dataframe & engineering features...')
    brca = df.drop_duplicates()
    #convert to Numerical
    brca['diagnosis'] = brca['diagnosis'].replace({'M':0, 'B':1}) 
    #Remove outliers
    for i in [i for i in brca.columns]:
        if brca[i].nunique()>=12:
            Q1 = brca[i].quantile(0.15)
            Q3 = brca[i].quantile(0.85)
            IQR = Q3 - Q1
            brca = brca[brca[i] <= (Q3+(1.5*IQR))]
            brca = brca[brca[i] >= (Q1-(1.5*IQR))]
    brca = brca.reset_index(drop=True)
    final = brca[finallist]
    y = final['diagnosis'] 
    X = final.loc[:, final.columns != 'b']
    # Resample data
    xres, yres = sm.fit_resample(X, y)
    # Split the data (80:20) ratio
    X_train, X_test, y_train, y_test = train_test_split(xres, yres, test_size=0.20, random_state=42) 
    #Scale / normalize the data
    scale = StandardScaler()
    X_train = scale.fit_transform(X_train)
    X_test = scale.transform(X_test)
    #Reshape y for modeling
    y_train = np.array(y_train).ravel()
    y_test = np.array(y_test).ravel()
    print('Cleaning Complete!')
    return X_train, X_test, y_train, y_test