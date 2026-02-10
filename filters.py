import pandas as pd

# None values are default arguments. If no value is provided when the function is called, the filter will be skipped.
def filter_tracks(similar_tracks: pd.DataFrame, popularity = None, gender = None, region = None):

    filtered_df = similar_tracks.copy()
    
    if gender:
        if gender == 'gender-balance':
            female_artists = filtered_df[filtered_df['artist_gender'] == 'F']
            male_artists = filtered_df[filtered_df['artist_gender'] == 'M']
            gender_balance = min(len(female_artists), len(male_artists))

            balanced_tracks = pd.concat([female_artists.head(gender_balance), male_artists.head(gender_balance)])
            filtered_df = balanced_tracks

        else:
            filtered_df = filtered_df[filtered_df['artist_gender'] == gender]

    if popularity:
        filtered_df = filtered_df[filtered_df['artist_popularity'] <= int(popularity)]

    if region:
        # Ensures region is a list if a user checked several regions:
        if isinstance(region, str):
            region = [region]        

        filtered_df = filtered_df[filtered_df['artist_region'].isin(region)]

    return filtered_df
    