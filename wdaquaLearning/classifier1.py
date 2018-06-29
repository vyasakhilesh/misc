import numpy as np
import pylab as pl
import pandas as pd
from sklearn.model_selection import cross_val_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import time

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

newdata = pd.read_csv('questionFeature_withCls.csv', sep=';')
newdata = newdata.replace(np.nan, 0, regex=True)
#print newdata.describe()
#print(np.shape(newdata.values))
print newdata.shape
ComponentStartingIndex = 33
ComponentIndex = ComponentStartingIndex
NoOfComponents = 1
x_t = newdata.iloc[0:, 1:11]
#y_t = newdata.iloc[0:, ComponentStartingIndex + 0:ComponentStartingIndex +0 +1] #i = 0
y_t = newdata.iloc[0:, -1] #i = 0
X=x_t.as_matrix()
y=y_t.as_matrix()
print x_t.head(5)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.231478, random_state = 1)


from sklearn.svm import SVC
import numpy as np



np.random.seed(123)

clf1 = LogisticRegression()
clf2 = RandomForestClassifier()
clf3 = GaussianNB()
clf4=  DecisionTreeClassifier()
clf5 = SVC()

print('5-fold cross validation:\n')


for clf, label in zip([clf1, clf2, clf3, clf4, clf5], ['Logistic Regression', 'Random Forest', 'naive Bayes', 'DecisionTreeClassifier', 'SVC']):

    scores = cross_val_score(clf, X, y, cv=10, scoring='accuracy')
    #print scores
    print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))

#clf1.fit(X_train, y_train )
#print clf1.predict(X_test)

dict_classifiers = {
    "Logistic Regression": LogisticRegression(),
    "Nearest Neighbors": KNeighborsClassifier(),
    "Linear SVM": SVC(),
    "Gradient Boosting Classifier": GradientBoostingClassifier(),
    "Decision Tree": tree.DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators = 18),
    "Neural Net": MLPClassifier(alpha = 1),
    "Naive Bayes": GaussianNB()
}

no_classifiers = len(dict_classifiers.keys())

def batch_classify(X_train, Y_train, X_test, Y_test, verbose = True):
    df_results = pd.DataFrame(data=np.zeros(shape=(no_classifiers,4)), columns = ['classifier', 'train_score', 'test_score', 'training_time'])
    count = 0
    for key, classifier in dict_classifiers.items():
        t_start = time.clock()
        classifier.fit(X_train, Y_train)
        t_end = time.clock()
        t_diff = t_end - t_start
        train_score = classifier.score(X_train, Y_train)
        test_score = classifier.score(X_test, Y_test)
        df_results.loc[count,'classifier'] = key
        df_results.loc[count,'train_score'] = train_score
        df_results.loc[count,'test_score'] = test_score
        df_results.loc[count,'training_time'] = t_diff
        if verbose:
            print("trained {c} in {f:.2f} s".format(c=key, f=t_diff))
        count+=1
    return df_results

df_results = batch_classify(X_train, y_train, X_test, y_test)
print(df_results.sort_values(by='test_score', ascending=False))