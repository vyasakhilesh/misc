import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
import pandas as pd
from sklearn.model_selection import cross_val_predict
from sklearn import metrics
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import train_test_split

newdata = pd.read_csv('questionFeature_withRes.csv', sep=';')
newdata = newdata.replace(np.nan, 0.0, regex=True)
#print(np.shape(newdata.values))
ComponentStartingIndex = 33
ComponentIndex = ComponentStartingIndex
NoOfComponents = 1

for i in range(0, NoOfComponents):

    X_trainCV = newdata.iloc[0:, 1:33]
    y_trainCV = newdata.iloc[0:, ComponentStartingIndex + i:ComponentStartingIndex + i + 1]


    data = newdata.iloc[0:, 1:33]
    target = newdata.iloc[0:, ComponentStartingIndex + i:ComponentStartingIndex + i + 1]


    X_train, X_test, y_train, y_test = train_test_split(
    data, target, test_size = 0.231478, random_state = 1)

    print X_train.shape, X_test.shape, y_train.shape, y_test.shape

    #print y_train

    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    #model = regr.fit(X_train, y_train)
    model = regr.fit(X_trainCV, y_trainCV)

    # Make predictions using the testing set
    y_pred = regr.predict(X_test)
    print y_pred.shape

    print("Mean squared error: %.2f"
          % mean_squared_error(y_test, y_pred))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % r2_score(y_test, y_pred))
    print('Variance score: %.2f' % metrics.r2_score(y_test, y_pred))




    print "Model Score:", model.score(X_test, y_test)
    #
    scores = cross_val_score(model, X_trainCV, y_trainCV, cv=10)
    print "Cross - validated scores:", scores
    print "Cross - validated scores:", scores.mean()


    plt.scatter(y_test, y_pred)
    plt.xlabel("True Values")
    plt.ylabel("Predictions")
    #
    plt.xticks(())
    plt.yticks(())
    #plt.show()
