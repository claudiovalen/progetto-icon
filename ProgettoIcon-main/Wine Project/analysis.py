import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from main import models
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


plt.figure()
plt.tick_params(axis='x', which='major')
sb.countplot(x= 'quality', data=df)
plt.show()
#for i, col in enumerate(df.columns):
  #  plt.figure(figsize=(25,13))
  #  plt.tick_params(axis='x', which='major', labelsize=3.5)
   # sb.countplot(x= col, data=df)
   # plt.show()

for i, col in enumerate(df.drop('quality',axis=1)):
    plt.figure(i)
    sb.barplot(x='quality', y =col, data=df)
    #plt.scatter(x='quality', y =col, data=df)
    #plt.title(col + ' vs Quality')
    #plt.ylabel(col)
    #plt.xlabel('Quality')
    plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)


sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Accuracy VS Depth Random forest Plot
accuracy = []
ds = np.arange(1, 20)
for i in ds:
    clf = RandomForestClassifier(max_depth=i, random_state=10)
    clf.fit(X_train, Y_train)
    predictions = clf.predict(X_test)
    accuracy.append(accuracy_score(Y_test, predictions))

plt.plot(ds, accuracy)
plt.grid()
plt.title('Accuracy vs. Random Forest Depth')
plt.xlabel('Depth')
plt.ylabel('Accuracy')
plt.show()

# Accuracy VS KNN
scores = []
error = []
ks = np.arange(1, 20)
folds = 10
for k in ks:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, Y_train)
    predictions = knn.predict(X_test)
    scores.append(accuracy_score(Y_test,predictions))
    error.append(np.mean(predictions!= Y_test))

plt.plot(ks, scores, linewidth=4, markersize=10)
plt.grid()
plt.xlabel("K in K-nearest Neighbors")
plt.ylabel("Cross Validation Test Accuracy")
plt.show()
plt.plot(ks,error,linewidth=4, markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')
plt.show()

model= models(X_train,Y_train,X_test,Y_test)
for i in range(len(model)):
    cm = plot_confusion_matrix(model[i],X_test, Y_test)
    plt.show()

plt.figure(figsize=(10,9))
map =sb.heatmap(df.corr(), annot=True, cmap="YlGnBu",xticklabels=True, yticklabels=True)
map.set_yticklabels(map.get_yticklabels(), rotation=0, fontsize=8)
map.set_xticklabels(map.get_xticklabels(), rotation=45, fontsize=8, rotation_mode='anchor', ha='right')
plt.show()