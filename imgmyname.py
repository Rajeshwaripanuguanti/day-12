from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
name="rajii reddy"
text=(name+'') * 500
mask=np.array(Image.open("heart_img.webp"))
wordcloud=WordCloud(background_color="black",mask=mask,contour_color="red",contour_width=5,colormap="Reds").generate(text)
plt.figure(figsize=(8,8))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()