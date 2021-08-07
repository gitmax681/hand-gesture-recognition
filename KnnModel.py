from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from pandas import read_csv
import numpy
import json
from returnvideo import main

with open('config.json', 'r') as f:
    _d = json.load(f)
    labels = _d['labels']
    dataversion = _d['CurrentData']
data = read_csv(f'data/{dataversion}', sep=',')
y = data.iloc[:, -1]
X = numpy.array(data.iloc[:, 0:-1]).astype(numpy.float)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
main('knnModel', labels, model=model)
