import streamlit as st
import pickle 
import pandas as pd 
import requests


# '''
# tmdb api key :  91da3860e425b5eef872b90e259ddc5c
# add this website url    ?api_key=YOUR_KEY   to the below website link 
# https://api.themoviedb.org/3/movie/{movie_id}/images


# https://api.themoviedb.org/3/movie/530/images?api_key=91da3860e425b5eef872b90e259ddc5c




# "file_path": "/h5e3r12VwfUotN36fBr1DNeCD4n.jpg"
# poster_url = "https://image.tmdb.org/t/p/w500" + file_path


# '''

# url used by owner 
# https://api.themoviedb.org/3/movie/65?api_key=<api_key>&language=en-US
# https://api.themoviedb.org/3/movie/65?api_key=91da3860e425b5eef872b90e259ddc5c&language=en-US



def fetch_poster(movie_id):
   response =  requests.get("https://api.themoviedb.org/3/movie/{}?api_key=91da3860e425b5eef872b90e259ddc5c&language=en-US".format(movie_id))

   data = response.json()
   print(data)
   return   "https://image.tmdb.org/t/p/w500/" +data["poster_path"]


def recommend(movie):
    movie_index = movies[movies["title"] ==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    # print(movie_list)
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:

       #  movie_id = i[0]    poster_path error because of this 
        movie_id = movies.iloc[i[0]].movie_id
        




        recommended_movies.append(movies.iloc[i[0]].title)
        # print(movies.iloc[i[0]].title)
        # print(i[0])

        # fetch poster from API

        recommended_movies_poster.append(fetch_poster(movie_id))





    return recommended_movies,recommended_movies_poster



movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame( movies_dict)


similarity = pickle.load(open('similarity.pkl','rb'))



st.title("Movie Recommendation System")

selected_movie_name= st.selectbox(
    'How you would like to be contacted', movies["title"].values
)

if st.button('Recommend'):
    # st.write(selected_movie_name)
    names,posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)
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




# git init 
# git add .
# git commit -am "inital commit"
# git remote add origin https://github.com/Rishit29Ranjan/Movie-Recommendation-System.git
# git remote -v
# git push origin master 