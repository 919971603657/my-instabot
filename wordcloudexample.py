from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
string ="A future in which drones deliver our goods is not far off."
wordcloud = WordCloud(stopwords=STOPWORDS, background_color = 'white', width=1200, height=1000).generate(string)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()