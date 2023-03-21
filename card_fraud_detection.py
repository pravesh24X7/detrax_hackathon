
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec


data = pd.read_csv('creditcard.csv')
data.head()

print(data.shape)
print(data.describe())


fraud = data[data['Class']==1]
valid = data[data['Class']==0]

outlier_fraction = len(fraud)/float(len(valid))
print(outlier_fraction)

print('Fraud case: []'.format(len(data[data["Class"]==1])))
print('Valid Transactions: []'.format(len(data[data['Class']==0])))

print("Amount details of the fraudant transaction")
fraud.Amount.describe()

print("Amount details of the valid transaction")
valid.Amount.describe()

corrmat = data.corr()
fig = plt.figure(figsize=(12,9))
sns.heatmap(corrmat, vmax=.8, square=True)
plt.show()

X = data.drop(['Class'], axis=1)
Y = data["Class"]

print(X.shape)
print(Y.shape)

xdata = X.values
ydata = Y.values

from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(xdata, ydata, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()

rfc.fit(xtrain, ytrain)
ypred = rfc.predict(xtest)


