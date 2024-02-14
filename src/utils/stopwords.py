import re
import nltk
from nltk.corpus import stopwords

class Stopwords:
    def __init__(self):
        """Initialize the class and download stopwords if necessary."""
        try:
            self.stopwords = stopwords.words('portuguese')
        except LookupError:
            nltk.download('stopwords')
            self.stopwords = stopwords.words('portuguese')

    def __call__(self):
        """Return a list of Portuguese stopwords."""
        return self.stopwords

    def remove_stopwords(self, line):
        """Remove stopwords from a text."""
        words = re.findall(r'\b\w+\b', line)
        words = [word for word in words if word not in self.stopwords]
        return ' '.join(words)