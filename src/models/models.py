from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

class SubjectClassifierModel:
    def __init__(self):
        self.model = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', MultinomialNB()),
        ])

    def train(self, X, y):
        """Train the model with the given data."""
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)
        print(f"Model score: {self.model.score(X_test, y_test)}")

    def predict(self, X):
        """Predict the class of the given data."""
        return self.model.predict(X)

    def save(self, path):
        """Save the model to a file."""
        joblib.dump(self.model, path)