from nltk.corpus import stopwords
from nltk import word_tokenize
import re

if __name__ == "__main__":

    # #tipo3
    target = 'LG'
    x = 'VENTILADOR DE PIE PHILCO VPP2018 DE 20 PULGADAS'
    stop_words = frozenset(stopwords.words('spanish'))
    word_tokens = word_tokenize(target.lower())
    tokens = [w for w in word_tokens if not w in stop_words]
    print('tokens', tokens)
    #print(re.findall(r"(?=("+'|'.join(tokens)+r"))",x.lower()))
    if re.findall(r"(?=("+'|'.join(tokens)+r"))",x.lower()):
        print('encontro algo')
        print(re.findall(r"(?=("+'|'.join(tokens)+r"))",x.lower()))

    # #tipo1
    # target = 'AOC SMART TV HD 32" 32S5295/77G'
    # title = 'AOC SMART TV  32" 32S5295/77G'
    # print( target == title )

    #tipo2
    # target = 'AOC SMART TV HD 32" 32S5295/77G'
    # title = 'AOC SMART TV HD 32" 32S5295/77G'
    # stop_words = frozenset(stopwords.words('spanish'))
    
    # word_tokens = word_tokenize(target.lower())
    # tokens = [w for w in word_tokens if not w in stop_words]
    
    # title_tokens = word_tokenize(title.lower())
    # title_token = [w for w in title_tokens if not w in stop_words]
    
    # print('token' , tokens)
    # print('title_token', title_token)
    # check =  all(item in tokens for item in title_token)
    # print(check)

    x = None
    x = str(x)
    print(x)