import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.metrics import plot_confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('dataset/wine.csv')


df = df.dropna()
boolean = False
boolean = df.isnull().values.any()
print(boolean)

Y = df['quality']
X = df.drop('quality',axis=1)

print(Y.value_counts())
plt.figure()
plt.tick_params(axis='x', which='major')
sb.countplot(x= 'quality', data=df)
plt.show()


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Create a function within many Machine Learning Models
def models(X_train,Y_train,X_test,Y_test):

    #Using KNeighborsClassifier Method of neighbors class to use Nearest Neighbor algorithm
    knn= KNeighborsClassifier(p=1)
    knn.fit(X_train, Y_train)
    knn_pred = knn.predict(X_test)
    knn_classification = classification_report(Y_test,knn_pred)

    #Using RandomForestClassifier method of ensemble class to use Random Forest Classification algorithm
    forest = RandomForestClassifier(max_depth=11,random_state=10)
    forest.fit(X_train, Y_train)
    forest_pred = forest.predict(X_test)
    forest_classification = classification_report(Y_test,forest_pred)

    print('[1]K Nearest Neighbor Test Accuracy:')
    print(knn_classification)
    print('[6]Random Forest Classifier Test Accuracy:')
    print(forest_classification)

    return knn,forest









