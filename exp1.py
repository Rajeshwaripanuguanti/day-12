import nltk
import string
nltk.download('punkt')
nltk.download('punkt_tab')#removing special symbols and split words
nltk.download('stopwords')#remove common english words
nltk.download('wordnet')#convert non grammatical words to gramatical
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
ch='a'
text="""Machine Learining, Deep Learning and Natural Language Processing are the better algorithms playing key role in AI concepts"""

#split sentence into words
words=word_tokenize(text)
print(words)

#removing common english words and store in another list
stop_words=set(stopwords.words('english'))
filtered=[w for w in words if w.lower() not in stop_words]
print(filtered)

#remove special symbols
remove_pun=[w for w in filtered if w not in string.punctuation]
print(remove_pun)