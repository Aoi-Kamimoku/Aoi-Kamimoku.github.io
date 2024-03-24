import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from collections import Counter

book = epub.read_epub('/Users/khan/Downloads/置身事内 中国政府与经济发展-兰小欢.epub')
content = []

for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        soup = BeautifulSoup(item.content, 'html.parser')
        content.append(soup.get_text())
text = ' '.join(content)

import jieba
words = jieba.lcut(text)
filtered_words = [word for word in words if len(word) > 1 and not any(char.isdigit() for char in word)]

from pyecharts.charts import WordCloud
from pyecharts import options as opts

word_counts = Counter(filtered_words).most_common(50)

wordcloud = WordCloud()
wordcloud.add('', word_counts, word_size_range=[20, 100], shape='cloud')
wordcloud.render('/Users/khan/Downloads/wordcloud.html')
