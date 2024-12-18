# -*- coding: utf-8 -*-
"""Task_3_Code_Case.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BrCEAC5L50A5lVNRDFC94lL5yaWW_cvc

**Movie Recommendation System Using ML**
"""

# import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import difflib
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# load data
dataset=pd.read_csv('/content/movies.csv')

dataset.head()

dataset.shape

# feature selection

selected_features=['genres','keywords','tagline','cast','director']

#remove nulls
for feature in selected_features:
  dataset[feature]=dataset[feature].fillna('')

merged_features=dataset['genres']+''+dataset['keywords']+''+dataset['tagline']+''+dataset['cast']+''+dataset['director']
print(merged_features)

#convert to numerical data

vectorizer=TfidfVectorizer()
feature_vectors=vectorizer.fit_transform(merged_features)
print(feature_vectors)

# cosine similarity
similarity=cosine_similarity(feature_vectors)
print(similarity)

"""get movie from user and check"""

movie_title=input('Enter movie name : ')

list_movies=dataset['title'].tolist()
print(list_movies)

matched_movies=difflib.get_close_matches(movie_title,list_movies)
print(matched_movies)

matched_movie=matched_movies[0]
print(matched_movie)

index_movie=dataset[dataset.title==matched_movie]['index'].values[0]
print(index_movie)

#find list of matches movies
similarity_score=list(enumerate(similarity[index_movie]))
print(similarity_score)

sorted_matched_m=sorted(similarity_score,key= lambda x:x[1],reverse=True)
print(sorted_matched_m)

#print matched movies
print('movise matches your need : ')

i=1
for movie in sorted_matched_m:
  index=movie[0]
  title_index=dataset[dataset.index==index]['title'].values[0]
  if(i<15):
    print(i, ':',title_index)
    i+=1

# recommendation system

movie_title=input('Enter movie name : ')

list_movies=dataset['title'].tolist()
matched_movies=difflib.get_close_matches(movie_title,list_movies)
matched_movie=matched_movies[0]
index_movie=dataset[dataset.title==matched_movie]['index'].values[0]

similarity_score=list(enumerate(similarity[index_movie]))
sorted_matched_m=sorted(similarity_score,key= lambda x:x[1],reverse=True)

print('movise matches your need : ')

i=1
for movie in sorted_matched_m:
  index=movie[0]
  title_index=dataset[dataset.index==index]['title'].values[0]
  if(i<40):
    print(i, ':',title_index)
    i+=1