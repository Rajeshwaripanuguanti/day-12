import nltk
nltk.download('punkt')
nltk.download('punkt_tab')#removing special symbols and split words
nltk.download('stopwords')#remove common english words
nltk.download('wordnet')#convert non grammatical words to gramatical
nltk.download('movie_reviews')
from nltk.corpus import movie_reviews,stopwords
from nltk.tokenize import word_tokenize
import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#list = [x for x in arr]
document=[(list(movie_reviews.words(field)),category) for category in movie_reviews.categories() for field in movie_reviews.fileids(category)]
stop_words=set(stopwords.words('english'))
#frequent use words
all_words=nltk.FreqDist(w.lower() for w in movie_reviews.words())
#only 2000 words token
word_features=list(all_words)[:2000]
print(word_features)
text=''.join(word_features)*1
wordcloud=WordCloud(width=800,height=400,background_color='white').generate(text)
#display 
plt.figure(figsize=(10,5))
plt.imshow(wordcloud)
plt.show()


