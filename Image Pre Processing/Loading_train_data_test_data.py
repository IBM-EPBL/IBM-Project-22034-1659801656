# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N0oxC0za0dNIE01fJJIOizv7oNrbVp2y
"""

0 lines (7 sloc)  269 Bytes

# define path to train and test dir

trainingpath=r"dataset/spiral/training"
testingpath=r"dataset/spiral/testing"

#loading train and test data

print("[INFO] loading data...")
(X_train,Y_train)=load_split(trainingpath)
(X_test,Y_test)=load_split(testingpath)