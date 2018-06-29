from sklearn.cross_validation import KFold
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet, SGDRegressor, BayesianRidge
import numpy as np
import pylab as pl
import pandas as pd
from sklearn.model_selection import cross_val_score

newdata = pd.read_csv('questionFeature_withResTar.csv', sep=';')
newdata = newdata.replace(np.nan, 0, regex=True)
#print(np.shape(newdata.values))
ComponentStartingIndex = 33
ComponentIndex = ComponentStartingIndex
NoOfComponents = 1
x_t = newdata.iloc[0:, 1:26]
print x_t.shape
#y_t = newdata.iloc[0:, ComponentStartingIndex + 0:ComponentStartingIndex +0 +1] #i = 0
y_t = newdata.iloc[0:, -1] #i = 0
x=x_t.as_matrix()
y=y_t.as_matrix()
print y
a = 0.3
for name,met in [
        ('linear regression', LinearRegression()),
        ('lasso', Lasso(fit_intercept=True, alpha=a)),
        ('ridge', Ridge(fit_intercept=True, alpha=a)),
        ('elastic-net', ElasticNet(fit_intercept=True, alpha=a)),
        ]:
    #print type(x), type(y)
    #print x.shape, y.shape
    model = met.fit(x, y)
    # p = np.array([met.predict(xi) for xi in x])
    p = met.predict(x)
    e = p-y
    #print p.shape, e.shape
    total_error = np.dot(e,e)
    rmse_train = np.sqrt(total_error/len(p))

    kf = KFold(len(x), n_folds=10)
    err = 0
    for train,test in kf:
        met.fit(x[train],y[train])
        p = met.predict(x[test])
        e = p-y[test]
        err += np.dot(e,e)

    rmse_10cv = np.sqrt(err/len(x))
    print('Method: %s' %name)
    print('RMSE on training: %.4f' %rmse_train)
    print('RMSE on 10-fold CV: %.4f' %rmse_10cv)
    scores = cross_val_score(model, x, y, cv=10, scoring='r2') #explained_variance
    print "Cross - validated scores:", scores
    print "Cross - validated scores:", scores.mean()
    print "\n"
