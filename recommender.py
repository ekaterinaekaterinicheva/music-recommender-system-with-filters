import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Loading datasets
dataset_a_df = pd.read_csv('YOUR_PATH/Dataset_A.csv', encoding = 'latin-1', delimiter=';')
dataset_b_df = pd.read_csv('YOUR_PATH/Dataset_B.csv', delimiter=';')

# Selecting audio features columns
audio_features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'valence', 'tempo']
audio_features_matrix = dataset_b_df[audio_features]

def fetch_track_features(track_title, artist):
    # Normalizing the input to ensure the search is case-insensitive
    track_title = track_title.lower()
    artist = artist.lower()

    # Filtering the df
    search_match: pd.DataFrame = dataset_a_df[
        (dataset_a_df['name'].str.lower() == track_title) &
        (dataset_a_df['artists'].str.lower() == artist)
    ]

    # Returning the index of the query track
    if not search_match.empty:
        print(search_match[['name', 'artists']])
        return search_match[audio_features].iloc[[0]].values # [[0]] returns a df with 1 row, not a Series. values converts that df into a 2D NumPy array.It looses the column names & index.
        
    else:
        print('Sorry, no matches were found. Try again.')
        return None

def find_similar_tracks(track_title, artist, top_n=10):
    input_vector = fetch_track_features(track_title, artist) # Returning a query track as a vector

    if input_vector is None:
        return []

    # Computing cosine similarity between a query track and all tracks in dataset_b_df.
    # Cosine similarity expects a NumPy array.
    # flatten() is used when (1, N) (one to many) is compared. We copare 1 track to many tracks, so we can turn this matrix into a 1D array a list with similarity scores.
    cosine_similarity_matrix = cosine_similarity(input_vector, audio_features_matrix).flatten()

    # Getting similarity scores
    sim_scores = list(enumerate(cosine_similarity_matrix)) # list(enumerate) converts matrix to a list of tuples - (index, value)

    # Sorting by similarity
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1] # key=lambda x: x[1] tells py to use the 2nd item in each tuple as the sort key. reverse=True means "descending". 

    # Returning track names & artists
    recommendations = dataset_b_df.iloc[[i[0] for i in sim_scores]][['artist', 'song_name', 'artist_gender', 'artist_popularity', 'artist_region']] # extracts rec tracks from a df based on sim scores. i[0] - index of the track in a df. iloc[] returns the row.
    
    return recommendations

# Example:
# print(find_similar_tracks('Bad Liar', 'Imagine Dragons'))

