```python
from sklearn import tree

class AIModel:
    def __init__(self):
        self.clf = tree.DecisionTreeClassifier()

    def train(self, features, labels):
        self.clf = self.clf.fit(features, labels)

    def predict(self, features):
        return self.clf.predict(features)

    def save_model(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.clf, f)

    def load_model(self, filename):
        with open(filename, 'rb') as f:
            self.clf = pickle.load(f)
```
