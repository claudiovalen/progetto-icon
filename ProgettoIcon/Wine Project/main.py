import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier



df = pd.read_csv('../dataset/wine.csv')

print(df.head())

df = df.dropna()

Y = df['quality']
X = df.drop(columns=['quality','pH','residual sugar','density'],axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)



#Create a function within many Machine Learning Models
def models(X_train,Y_train,X_test,Y_test):

    #Using the Nearest Neighbor algorithm
    knn = KNeighborsClassifier(p=1)
    knn.fit(X_train, Y_train)
    knn_pred = knn.predict(X_test)
    knn_classification = classification_report(Y_test,knn_pred)

    #Using the Random Forest Classification algorithm
    forest = RandomForestClassifier(max_depth=11,random_state=10)
    forest.fit(X_train, Y_train)
    forest_pred = forest.predict(X_test)
    forest_classification = classification_report(Y_test,forest_pred)

    print('[0]K Nearest Neighbor Test Accuracy:')
    print(knn_classification)
    print('[1]Random Forest Classifier Test Accuracy:')
    print(forest_classification)

    return knn,forest


df_empty = df[0:0]
df_empty = df_empty.drop(columns=['quality','pH','residual sugar','density'],axis=1)

Y_KB = df['quality']

