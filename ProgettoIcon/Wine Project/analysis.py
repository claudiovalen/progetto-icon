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

df = pd.read_csv('../dataset/wine.csv')

df = df.dropna()

Y = df['quality']
X = df.drop(columns=['quality','pH','residual sugar','density'],axis=1)


# Count quality
plt.figure()
plt.tick_params(axis='x', which='major')
sb.countplot(x='quality', data=df)
plt.show()

# Heatmap
plt.figure(figsize=(10,9))
map =sb.heatmap(df.corr(), annot=True, cmap="YlGnBu",xticklabels=True, yticklabels=True)
map.set_yticklabels(map.get_yticklabels(), rotation=0, fontsize=8)
map.set_xticklabels(map.get_xticklabels(), rotation=45, fontsize=8, rotation_mode='anchor', ha='right')
plt.show()

# Quality vs other columns
for i, col in enumerate(df.drop('quality',axis=1)):
    plt.figure(i)
    sb.barplot(x='quality', y =col, data=df)
    plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

# Standardize
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Accuracy VS Depth Random forest Plot
accuracy = []
error = []
interval = np.arange(1, 20)
for i in interval:
    clf = RandomForestClassifier(max_depth=i, random_state=10)
    clf.fit(X_train, Y_train)
    predictions = clf.predict(X_test)
    accuracy.append(accuracy_score(Y_test, predictions))
    error.append(np.mean(predictions!= Y_test))


plt.plot(interval, accuracy, linewidth=4, markersize=10)
plt.grid()
plt.title('Accuracy vs. Random Forest Depth')
plt.xlabel('Depth')
plt.ylabel('Accuracy')
plt.show()
plt.plot(interval,error,linewidth=4, markersize=10)
plt.title('Error Rate Depth Value')
plt.xlabel('Depth Value')
plt.ylabel('Mean Error')
plt.show()


# Accuracy VS KNN
scores = []
error = []
for k in interval:
    knn = KNeighborsClassifier(p=k)
    knn.fit(X_train, Y_train)
    predictions = knn.predict(X_test)
    scores.append(accuracy_score(Y_test,predictions))
    error.append(np.mean(predictions!= Y_test))

plt.plot(interval, scores, linewidth=4, markersize=10)
plt.grid()
plt.title('Accuracy vs. KNN')
plt.xlabel("K in K-nearest Neighbors")
plt.ylabel("Cross Validation Test Accuracy")
plt.show()
plt.plot(interval,error,linewidth=4, markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')
plt.show()

#CLassification Report and Confusion Matrix
model= models(X_train,Y_train,X_test,Y_test)
for i in range(len(model)):
    cm = plot_confusion_matrix(model[i],X_test, Y_test)
    plt.show()

