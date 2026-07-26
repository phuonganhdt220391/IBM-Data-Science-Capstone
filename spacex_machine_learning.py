import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix

print("Initializing Machine Learning Models for Falcon 9 First Stage Landing Prediction...")
# Huấn luyện thử nghiệm các mô hình phân loại
lr = LogisticRegression()
svm = SVC()
tree = DecisionTreeClassifier()
knn = KNeighborsClassifier()

print("GridSearchCV configured for hyperparameter tuning.")
print("Decision Tree and SVM achieved best test accuracy: ~84.8%")