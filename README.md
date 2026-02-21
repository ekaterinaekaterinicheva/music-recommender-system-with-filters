# Music Recommender App
This is a content-based **music recommender system** with user-controlled **filters for fairness and diversity**.

## How Does It Work?
Let’s assume a user wants to find songs that sound similar to “Help!” by The Beatles.

In the original version of the application, the user manually entered:
- the **exact song title**
- the **exact artist name**

and configured additional filters such as:
  - popularity (e.g., less mainstream artists),
  - gender (e.g., female artists),
  - region (e.g., European artists).

On the server side, the system follows the following steps:
1. The application looks up “Help!” by The Beatles in **Dataset A**, which is a large catalogue of songs containing structured **audio feature vectors** (e.g., energy, danceability, etc.).
2. The selected song’s feature vector is compared against audio feature vectors of the songs in **Dataset B**, which is a music recommendation catalogue for fairness and diversity.
3. Similarity is computed using **cosine similarity**, which measures the angle between two audio feature vectors - the smaller the angle, the higher the similarity.
4. The top 10 most similar tracks are selected and ranked.
5. User-selected filters (popularity, gender, region) are applied using conditional logic before returning the results.

## App Screenshots (Original Version)
### App showing recommendations after manual user input and filter settings were applied
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/28cac049-31df-422a-8d76-e27049a0296a" />

### App showing a message notifying that no songs matched the applied filters
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/cb1ab34b-b243-4cb1-a386-f030999b59a0" />

## System Architecture
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/69b16392-7365-4335-9d2f-87d633983ca2" />

## Update: Autocomplete Search & "Try Demo Recommendation" Button
### Reason for the update
In the original version, users were required to manually input the exact spelling of a song and artist from Dataset A.
Since Dataset A is a large music catalogue, this created difficulties for users (especially when the application was deployed) because they would need to browse the dataset to know valid inputs.

### New Features
To address this usability limitation and improve the demo experience, the system was improved with two features:
- **Autocomplete Search**
Autocomplete dynamically suggests valid song–artist pairs from Dataset A as the user types, removing the need to manually browse the full music catalogue.

The autocomplete **logic**:
1. It queries Dataset A while the user types
2. It returns unique song–artist pairs
3. It automatically fills both fields when selected
   
- **"Try Demo Recommendation" Button**
The demo button automatically fills the input fields with Help! by the Beatles, selects certain filter configurations, and immediately generates recommendations, allowing users to explore the recommender’s functionality.

The button allows users, especially **first-time users** to:
1. See how the system works in seconds
2. Observe filter behavior
3. Evaluate ranking logic

## App Screenshots (Updated Version)
### New Features Implemented in the Music Recommender App: Autocomplete Search and "Try Demo Recommendations" Button
<img width="600" height="600" alt="Music_Recommender_App_New_Version" src="https://github.com/user-attachments/assets/7da6ca97-0dbf-4dc8-84c0-b4fa8d2e6d03" />

### Autocomplete Search in Action
<img width="600" height="600" alt="Music_Recommender_App_Autocomplete" src="https://github.com/user-attachments/assets/61908aae-6f53-4819-b052-41167e0dc359" />

### Impact of the Update
- These improvements allowed the application to transition from a prototype into a production-ready interactive ML web application.
- The **user experience has been significantly improved**, making the system more robust and accessible.

## App Installation and Setup
This project requires two specific datasets. While these were originally public, they have been pre-processed to ensure audio feature vectors are formatted correctly for computing cosine similarity.

1. Download the Datasets
Please download the following datasets and ensure they are saved in .csv format:
- [Dataset A](https://drive.google.com/file/d/1Akz2p3eXFY-FGYoRKJk-g_hP1cZ1Rz84/view?usp=drive_link): Used for selection of the songs based on which recommendations will be suggested
- [Dataset B](https://drive.google.com/file/d/1_YFcLwIcb9GcTre4NkB_sSo4U4vZlyEG/view?usp=drive_link): The recommendation catalogue

2. Link the Datasets to the Code
Once downloaded, you need to link the datasets to the app. Open recommender.py and update the path strings in the following lines:
```
#Loading datasets
dataset_a_df = pd.read_csv('YOUR_PATH_TO_Dataset_A.csv', encoding='latin-1', delimiter=';')
dataset_b_df = pd.read_csv('YOUR_PATH_TO_Dataset_B.csv', delimiter=';')
```
Please note that the latin-1 encoding and semi-colon (;) delimiters are required for these datasets to be parsed correctly due to the applied pre-processing.

3. Launch the Music Recommender App

Click on 'Run Python File' (or run app.py) to let Flask to initialize and host the app on a local production server.

Click on the generated URL and start exploring music recommendations, enjoying the balance of diversity and fairness while discovering new, unexpected songs and artists! :musical_note: :microphone:

