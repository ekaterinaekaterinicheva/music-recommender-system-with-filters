import pandas as pd
import gdown
import os
from sklearn.metrics.pairwise import cosine_similarity

# Checking if we are on Render
IS_PROD = os.getenv('RENDER') # Render sets this variable to 'true'

def get_dataset(local_path, file_id, **kwargs):
    if IS_PROD:
    # Downloading datasets from Google Drive
        file_name = os.path.basename(local_path)
        if not os.path.exists(file_name):     
            print(f"Downloading {file_name} from Google Drive...")
            url = f'https://drive.google.com/uc?id={file_id}'
            gdown.download(url, file_name, quiet=False)
        return pd.read_csv(file_name, **kwargs)
    else:
        # If we are local, use the computer's path
        return pd.read_csv(local_path, **kwargs)

# Loading datasets
dataset_a_df = get_dataset(
    local_path = 'C:/Users/1ekat/Desktop/Music_Recommender/data/Dataset_A.csv',
    file_id ='1Akz2p3eXFY-FGYoRKJk-g_hP1cZ1Rz84', 
    encoding='latin-1', 
    delimiter=';'
)

dataset_b_df = get_dataset(
    local_path = 'C:/Users/1ekat/Desktop/Music_Recommender/data/Dataset_B.csv',
    file_id='1_YFcLwIcb9GcTre4NkB_sSo4U4vZlyEG', 
    delimiter=';'
)

# Selecting audio features columns
audio_features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'valence', 'tempo']
audio_features_matrix = dataset_b_df[audio_features]

# Automcomplete while typing in
def search_songs(query):
    q = query.lower()

    results = (
        dataset_a_df[
            dataset_a_df["name"].str.lower().str.contains(q) |
            dataset_a_df["artists"].str.lower().str.contains(q)
        ][["name", "artists"]]
        .drop_duplicates()
        .head(10)
        .rename(columns={"artists": "artist"})
    )

    return results.to_dict(orient="records")

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

