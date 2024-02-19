import streamlit as st

import pandas as pd
import numpy as np
import requests

TEST_DATA_FILE='movies.csv'
movies=pd.read_csv(TEST_DATA_FILE)


similarity=np.genfromtxt("similarity5.csv", delimiter=",")

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=df8347a5ba2d1d46a17fdbb2e63a260e'.format(movie_id))
    data=response.json()
    print(data)
    return 'https://image.tmdb.org/t/p/original'+data['poster_path']

def recommend(movie):
    movie_idx=movies[movies['title']==movie].index[0]
    distances=similarity[movie_idx]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movie_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))
    return recommended_movies ,recommended_movie_poster  

st.title("Movie Recommendation System")
selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'])

if st.button('recommend'):
    names,posters=recommend(selected_movie_name)
    
#st.write('You selected:', option)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
       st.text(names[0])
       st.image(posters[0])
   
    with col2:
       st.text(names[1])
       st.image(posters[1])
    
    with col3:
       st.text(names[2])
       st.image(posters[2])
    
    with col4:
       st.text(names[3])
       st.image(posters[3])
    
    with col5:
       st.text(names[4])
       st.image(posters[4])
    
      
