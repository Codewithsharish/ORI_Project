# -*- coding: utf-8 -*-
"""ORI_Assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nPpWFrM-VKi56cA2jjiPBgjHU7rZunl2
"""

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import spacy

file_path = '/content/Evaluation-dataset.csv'
df = pd.read_csv(file_path)

df.head()

df.tail()

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nlp = spacy.load('en_core_web_sm')

positive_words = set(['Good', 'Great', 'Excellent', 'Amazing', 'Easy', 'Awesome', 'Positive'])
negative_words = set(['Bad', 'Poor', 'Horrible', 'Wrong', 'Missing', 'Difficult', 'Expensive', 'Incorrect'])

def preprocess_text(text):
  tokens = word_tokenize(text.lower())
  tokens = [word for word in tokens if word.isalpha()]
  tokens = [word for word in tokens if word not in stopwords.words('english')]
  lemmatizer = WordNetLemmatizer()
  tokens = [lemmatizer.lemmatize(word) for word in tokens]
  return tokens

def extract_subthemes(text):
  subthemes = []
  doc = nlp(text)
  for token in doc:
    if token.text in['garage', 'service']:
      subthemes.append('garage service')
    elif token.text in['wait', 'time', 'delay']:
      subthemes.append('wait time')
    elif token.next in['incorrect', 'tyres', 'sent', 'missing']:
      subthemes.append('incorrect tyres sent')
  return subthemes

def analyze_sentiment_custom(text):
  tokens = word_tokenize(text.lower())
  positive_score = sum(1 for token in tokens if token in positive_words)
  negative_score = sum(1 for token in tokens if token in negative_words)
  if positive_score > negative_score:
    return 'positive'
  elif negative_score > positive_score:
    return 'negative'
  else:
    return 'neutral'

def analyze_review_custom(review):
  subthemes = ["theme1", "theme2"]
  sentiments = ["positive", "negative"]
  return {"subthemes":subthemes,"sentiments":sentiments}

import pandas as pd
data = pd.DataFrame({'Reviews':["Quick and simple website from which to choose the tyres I wanted. Good value, good quality tyres. Whole process from choice to fitting was easy."]})

def analyze_review_custom(review):
  positive_words = ['Easy', 'Excellent']
  if any (word in review.lower() for word in positive_words):
    return {'subthemes': 'theme1', 'sentiments': 'Postive'}
  else:
    return {'subthemes': 'theme2', 'sentiments': 'Negative'}

data['Predicted_Subthemes_sentiments'] = data['Reviews'].apply(analyze_review_custom)

output_path = '/content/Evaluation-dataset.csv'
data.to_csv(output_path, index=False)

print(data[['Predicted_Subthemes_sentiments']].head())