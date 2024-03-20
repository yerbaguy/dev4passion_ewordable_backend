import spacy
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

porter = PorterStemmer()
wordnet = WordNetLemmatizer()

nlp = spacy.load('en_core_web_sm')
#doc = nlp("thisview")
doc = nlp('thisview')

mystring1 = ["this","that","of"]
mystring = "thisview"

mystring2 = ["thisview","thatview"]
words = []


for token in doc:
    print(token.text, token.lemma_, token.pos_ , token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)


for tok in doc:
    print(tok)

if "this" in mystring:
    print("OK")

string = mystring.split()
print(string)

text = mystring.removeprefix("this")
print(text)

for mystrin in mystring1:
    print(mystrin)

for mystrinn in mystring1:
    if mystrinn in mystring:
        print("yes")
        str = mystring.removeprefix(mystrinn)
        print(str)


for mystrinn in mystring1:
    #somestring=""
    str = ""
    strr = ""
    for mystri in mystring2:
        if mystrinn in mystri:
            print("yessss")
            str = mystri
            print(str)
            #strr = mystring.removeprefix(mystrinn)
            strr = str.removeprefix(mystrinn)
            words = strr
            print(strr)
            print(words)
            #print(str)
            #words = mystrinn
            #str1 = mystring2.remove(mystrinn)
            #print(str)
            
            #print(strr)
            #print(mystri)
          

          # print(mystrinn)

tokenized_docs_no_stop_words = []


for doc in mystring2:
    new_term_vector = []
    for word in doc:
        if not word in stopwords.words('english'):
            new_term_vector.append(word)

    tokenized_docs_no_stop_words.append(new_term_vector)

print(tokenized_docs_no_stop_words)




preprocessed_docs = []

for doc in mystring2:
    final_doc = []
    for word in doc:
       # final_doc.append(porter.stem(word))
        final_doc.append(wordnet.lemmatize(word))

preprocessed_docs.append(final_doc)

print(preprocessed_docs)
