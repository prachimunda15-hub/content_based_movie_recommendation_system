import streamlit as st
import pickle
import pandas as pd



def recommend(movie_name):
    movies_df = pd.DataFrame(movies_dict)
    movie = movie_name.replace(" ", "")
    matches = movies_df[movies_df['Title'] == movie]



    movie_index = matches.index[0]

    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances))
                        , reverse=True,
                        key=lambda x: x[1])[1:6]
    recommended_movie =[]
    for i in movie_list:
        recommended_movie.append(movies_df.iloc[i[0]]['Title'])
    return recommended_movie

with open('movies_dict.pkl', 'rb') as f:
    movies_dict = pickle.load(f)

movie=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommender System")
selected_movie_name = st.selectbox('Movie Name ',movie['Title'].values)
if st.button('Recommend'):
    recommendations =  recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)



