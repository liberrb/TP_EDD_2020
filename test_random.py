from nltk.corpus import stopwords
from nltk import word_tokenize
import re

if __name__ == "__main__":

    target = 'SAMSUNG'
    x = 'SMART TV SAMSUNG 65 PULGADAS 4K UHD 65RU7100'
    stop_words = frozenset(stopwords.words('spanish'))
    word_tokens = word_tokenize(target.lower())
    tokens = [w for w in word_tokens if not w in stop_words]
    print(tokens)
    print(re.findall(r"(?=("+'|'.join(tokens)+r"))",x.lower()))
    if re.findall(r"(?=("+'|'.join(tokens)+r"))",x.lower()):
        print('encontro algo')