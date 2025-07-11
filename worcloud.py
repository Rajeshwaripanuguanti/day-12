from wordcloud import WordCloud
import matplotlib.pyplot as plt
text="""Machine Learining, Deep Learning and Natural Language 
Processing are the better algorithms playing key role in AI concepts"""
#creating wordcloud
wordcloud=WordCloud(width=800,height=400,background_color='blue').generate(text)
#display 
plt.figure(figsize=(10,5))
plt.imshow(wordcloud)
plt.show()