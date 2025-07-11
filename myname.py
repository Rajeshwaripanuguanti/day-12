from wordcloud import WordCloud
import matplotlib.pyplot as plt
my_name="rajeshwari"
hashtags=["#Technical Trainer","#Full stack Developer",
"#Corparate Trainer","#Mobile App developer",
"#freelauncer","#Cool person",
"#Technical Trainer","#Full stacker","#Corporate Trainer",
"#Mobile App developer","#freelauncer","#Cool person"]
text=(my_name+' ')*100+' '.join(hashtags*5)
wordcloud=WordCloud(width=1000,height=500,background_color='white',colormap='viridis').generate(text)
plt.figure(figsize=(14,6))
plt.imshow(wordcloud,interpolation='bilinear')
plt.show()