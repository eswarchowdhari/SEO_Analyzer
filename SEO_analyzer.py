import pandas as pd
import requests
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import streamlit as st
from bs4 import BeautifulSoup

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


st.title('SEO Analyzer')
url = st.text_input('Enter URL')

def seo_analyzer(url):
    
    
    res = requests.get(url)
    if res.status_code != 200:
        st.error("Error: Unable to access the Website.")
        return

    soup = BeautifulSoup(res.content, 'html.parser')

    bad = []
    good = []
    keywords = []

    
    title = soup.find('title')
    if title and title.text:
        good.append(f"Title Exists: {title.text}")
    else:
        bad.append("No Title!")

    meta_d = soup.find('meta', attrs={'name': 'description'})
    if meta_d and 'content' in meta_d.attrs:
        meta_d_content = meta_d['content']
        good.append(f"Meta Description Exists: {meta_d_content}")
        if len(meta_d_content) >= 150:
            good.append("It's a good Description")
        else:
            bad.append("The Description is not sufficient")
    else:
        bad.append("No Meta Description!")

    
    hs = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    h_tags = []
    for h in hs:
        headings = soup.find_all(h)
        for heading in headings:
            good.append(f"{heading.name}--->{heading.text.strip()}")
            h_tags.append(heading.name)

    if 'h1' not in h_tags:
        bad.append("No H1 found!")

    
    for img in soup.find_all('img'):
        if not img.get('alt'):  # Checks if 'alt' attribute is absent or empty
            bad.append(f"No Alt text for image: {img}")

    
    bod = soup.find('body').text
    words = [i.lower() for i in word_tokenize(bod)]
    
    bi_grams = ngrams(words, 2)
    freq_bigrams = nltk.FreqDist(bi_grams)
    bi_grams_freq = freq_bigrams.most_common(10)

    
    sw = nltk.corpus.stopwords.words('english')
    new_words = [i for i in words if i not in sw and i.isalpha()]
    freq = nltk.FreqDist(new_words)
    keywords = freq.most_common(10)

    
    tab1, tab2, tab3, tab4 = st.tabs(['Keywords', 'BiGrams', 'Good', 'Bad'])
    with tab1:
        for i in keywords:
            st.text(i)
    with tab2:
        for i in bi_grams_freq:
            st.text(i)
    with tab3:
        for i in good:
            st.text(i)
    with tab4:
        for i in bad:
            st.text(i)

seo_analyzer(url)
