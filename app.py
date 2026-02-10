# Flask is a web framework that allows to build web apps.
# Flask request is a module used to access the data sent from the user to the server and pass these data to the app.

from flask import Flask, request, jsonify, render_template
from filters import filter_tracks
from recommender import find_similar_tracks

# Creating an application
app = Flask(__name__)

# Creating an endpoint/a route for the start page
@app.route('/')
def start():
    return render_template('index.html')

# Creating an endpoint/a route for the recommendations page
@app.route('/recommendations', methods=['POST'])
def recommend(): # Maps this function to the route '/recommendations'    
    data = request.get_json() # Parses the incoming JSON request and converts it into a Python dictionary.
    track_title = data.get('title')
    artist = data.get('artist')
    popularity = data.get('popularity') # 'popularity' is a key in the JSON object being sent.
    gender = data.get('gender')
    region = data.get('region', [])

    similar_tracks = find_similar_tracks(track_title, artist) # Returns a df.
    recommended_tracks = filter_tracks(similar_tracks, popularity = popularity, gender = gender, region = region)

    message = ""
    if recommended_tracks.empty:
        message = "Sorry, no matches were found... Please try again."

    result = recommended_tracks[['song_name', 'artist']].to_dict(orient='records')  # converts the df to a dictionary; 'records’ : list like [{column -> value}, … , {column -> value}]

    return jsonify({'result': result, 'message': message})



# ! Checks if the current script is being run directly as the main program,
# or if it's being imported as a module into another program:
if __name__ == '__main__':
    app.run(debug=True) # With(debug=True) there's no need to constantly restart the server when changes have been made (Once the app is deployed -> (debug=False)).

