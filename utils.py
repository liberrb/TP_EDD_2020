
from nltk.corpus import stopwords
from nltk import word_tokenize
import re

class Utils():

    def tipo_busqueda_1(self, target, title):
        return target.lower() == title.lower()

    def tipo_busqueda_2(self, target, title):
        # target = self.stop_words(target)
        # title = self.stop_words(title)
        # return all(item in target for item in title)

        target = self.stop_words(target)
        title = self.stop_words(title)
        equals = set(target) & set(title)
        return len(target) == len(equals)

    def tipo_busqueda_3(self, target, title):
        target = self.stop_words(target)
        title = self.stop_words(title)
        return any(item in target for item in title)

    def stop_words(self, text):
        stop_words = frozenset(stopwords.words('spanish'))
        text_tokens = word_tokenize(text.lower())
        tokens = [w for w in text_tokens if not w in stop_words]
        return tokens
