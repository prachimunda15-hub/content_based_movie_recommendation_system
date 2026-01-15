Table Of Content  
* Overview
* Features
* Approach
* Dataset
* Model Implementation
* Contributing
* License
* Acknowledgements


Overview 
This model is used to recommend movies based on users' interests. Its main goal is to help users find movies they might enjoy, reducing the time and effort needed to search through large catalogs.

Feature 
* Recommends movies similar to the ones the user likes or searched.
* Uses genre,cast,crew,plot.

Approach 
This model  is  content based recommendation system. The recommends movies based on movie features and user preferences.Example:
If a user likes Interstellar, the system recommends Inception and The Martian.


Dataset - https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows

Model Implementation 

The Movie Recommendation System is implemented using a content-based filtering approach, which recommends movies by measuring the similarity between movie features. The implementation follows the steps outlined below: 

* Data Collection
 * A movie dataset is used containing relevant metadata such as:
 * Movie title
 * Genres
 * Overview / description
 * Cast
 * Director

* Data Preprocessing
  Selected important features are combined into a single textual representation.
  Missing values are handled by replacing them with empty strings.
  Text data is cleaned by converting to lowercase and removing unnecessary symbols.

* Feature Extraction

   from sklearn.feature_extraction.text import CountVectorizer

  cv = CountVectorizer(max_features = 7000,stop_words ='english')
  * CountVectorizer converts a collection of text documents into a matrix of token (word) counts.
  * max_features=7000
    Keeps only the 7,000 most frequent words across the corpus (helps limit dimensionality).
  * stop_words='english'
     Automatically removes common English stop words like the, is, and, to, etc.

* Similarity Computation
Cosine similarity is used to measure similarity between movies.
Higher cosine values indicate more similar movie content.
from sklearn.metrics.pairwise import cosine_similarity, 
similarity = cosine_similarity(vectors) 

* Recommendation Generation
When a user selects a movie, the system retrieves its index.Similarity scores are sorted in descending order.The top N most similar movies are recommended.

def recommend (movie_name):
  
  movie = movie_name.replace(" ", "")
  matches = new_data[new_data['Title'] == movie]
  
  if matches.empty:
        print("Movie not found in dataset")
        return

  movie_index = matches.index[0]
    
  distances =similarity[movie_index]
  movie_list = sorted(list(enumerate(distances))
                        ,reverse = True,
                       key=lambda x: x[1])[1:5]
  for i in movie_list:
       print(new_data.iloc[i[0]].Title)
  
* User Interface Integration
   * The model is integrated into a Streamlit web application
   * Users can select a movie from a dropdown and instantly receive recommendations

* License
* 
