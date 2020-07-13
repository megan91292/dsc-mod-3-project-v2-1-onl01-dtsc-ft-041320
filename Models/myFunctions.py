import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import xgboost as xgb

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score,f1_score

from sklearn.metrics import make_scorer
from sklearn.linear_model import LogisticRegression 

from imblearn.over_sampling import SMOTE

def plot_confusion_matrix(y_test,y_test_preds,data='test'):
    cm_test = confusion_matrix(y_test,y_test_preds)
    print(f"{cm_test[1][0]/cm_test.sum()*100} of False Negatives")
    sns.heatmap(cm_test,cmap=sns.color_palette('Blues'),fmt ='.1f',annot=True)
    plt.ylim([2,0])
    plt.title(f"Confusion Matrix\n{data} Data")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()
    
    
def print_metrics(labels, preds):
    print("Precision Score: {}".format(precision_score(labels, preds)))
    print("Recall Score: {}".format(recall_score(labels, preds)))
    print("Accuracy Score: {}".format(accuracy_score(labels, preds)))
    print("F1 Score: {}".format(f1_score(labels, preds)))
    

def plot_feature_importances(model):
    n_features = X_train.shape[1]
    plt.figure(figsize=(8,8))
    plt.barh(range(n_features), model.feature_importances_, align='center') 
    plt.yticks(np.arange(n_features), X_train.columns.values) 
    plt.xlabel('Feature importance')
    plt.ylabel('Feature')

