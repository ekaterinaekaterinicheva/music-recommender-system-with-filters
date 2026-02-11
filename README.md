# Music Recommender App
This is a content-based **music recommender system** with user-controlled **filters for fairness and diversity**

## How Does It Work?
Let’s suggest that the user wants to find songs that have a **similar sound** to the song Help! by the Beatles. So, the user enters the song and the singer. The user also wants to see not so popular singers in recommendations, so they adjust the **popularity filter**, along with the **gender** and **region**.

On the server side, the system looks up the song Help! by the Beatles in **Dataset A**. This is a big catalogue that stores songs together with their *audio features* – numbers describing things like energy, danceability, etc. These features are then compared to songs in **Dataset B**, which is a smaller catalogue of songs. The system measures how similar the songs are to the song Help! by the Beatles using cosine similarity, which checks how close 2 songs are by comparing their feature vectors: the smaller the angle between them, the more similar they are. The system selects 10 similar songs and ranks them.

The filters the user selects are applied through simple if–else rules.

## App Screenshots
### App showing recommendations after user input and filter settings were applied
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/28cac049-31df-422a-8d76-e27049a0296a" />

### App showing a message notifying that no songs matched the applied filters
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/cb1ab34b-b243-4cb1-a386-f030999b59a0" />

## System Architecture
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/69b16392-7365-4335-9d2f-87d633983ca2" />

## Data Setup
This project requires two specific datasets. While these were originally public, they have been pre-processed to ensure audio feature vectors are formatted correctly for computing cosine similarity.

**1. Download the Datasets**
Please download the following datasets and ensure they are saved in .csv format:
- [Dataset A](https://drive.google.com/file/d/1Akz2p3eXFY-FGYoRKJk-g_hP1cZ1Rz84/view?usp=drive_link): Used for selection of the songs based on which recommendations will be suggested
- [Dataset B](https://drive.google.com/file/d/1_YFcLwIcb9GcTre4NkB_sSo4U4vZlyEG/view?usp=drive_link): The recommendation catalogue

**2. Link the Datasets to the Code**
Once downloaded, you need to link the datasets to the app. Open recommender.py and update the path strings in the following lines:
```
#Loading datasets
dataset_a_df = pd.read_csv('YOUR_PATH_TO_DATASET_A.csv', encoding='latin-1', delimiter=';')
dataset_b_df = pd.read_csv('YOUR_PATH_TO_DATASET_B.csv', delimiter=';')
```
Please note that the latin-1 encoding and semi-colon (;) delimiters are required for these datasets to be parsed correctly due to the applied pre-processing.

## Launching the Music Recommender App
You are all set! :blush: Once you have configured the file paths and installed the necessary dependencies, you only need to:
1.	Click on 'Run Python File' (or run app.py). Flask will initialize and host the app on a local production server.
2.	Click on the generated URL.
3.	Go and explore music, enjoying the balance of diversity and fairness while discovering new, unexpected songs and artists! :musical_note: :microphone:

