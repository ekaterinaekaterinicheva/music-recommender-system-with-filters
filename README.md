# Music Recommender System  With Filters For Fairness & Diversity
This is a **content-based** music recommender system with user-controlled filters promoting **fairness** and **diversity**.

Try [DEMO](https://music-recommender-system-with-filters.onrender.com/) on Render

## How Does It Work?
Let’s assume a user wants to find songs that sound similar to “Help!” by The Beatles.

In the original version of the application, the user manually entered:
- the **exact song title**
- the **exact artist name**
  
and configured filters such as:
- popularity (e.g., less mainstream artists),
- gender (e.g., female artists),
- region (e.g., European artists).

On the server side, the system performs the following steps:
1. The application looks up “Help!” by The Beatles in **Dataset A**, which is a large catalogue of songs containing audio feature vectors (e.g., energy, danceability, etc.).
2. The selected song’s **audio feature vector** is compared against audio features of the songs located in **Dataset B**, which is a recommendation catalogue for fairness & diversity.
3. Similarity is computed using **cosine similarity**, which measures the angle between two audio feature vectors: the smaller the angle, the higher the similarity.
4. The top-10 most similar songs are selected and ranked.
5. User-selected filters (popularity, gender, region) are applied using conditional logic before returning the results to the user.

## App Screenshots (Original Version)
### App showing recommendations after manual user input and filter configurations were applied
<img width="600" height="600" alt="App_Showing_Recs_After_Manual_User_Input" src="https://github.com/user-attachments/assets/8f2fc899-6d78-4bef-801e-defeda1a1b8c" />

### App showing a message notifying that no songs matched the applied filters
<img width="600" height="600" alt="App_Showing_A_No_Matches_Found_Message" src="https://github.com/user-attachments/assets/644eeefa-aece-417f-9a5f-1670daa98e91" />

## System Architecture
<img width="600" height="600" alt="System_Architetcure" src="https://github.com/user-attachments/assets/8d0a6a77-b58d-4701-879c-e346e578bfa5" />

## Deployment and Demo
The application is **live** and can be tested here: https://music-recommender-system-with-filters.onrender.com/

**Note:** This demo is hosted on Render using Free plan, which has limited RAM (512MB). Due to the large size of the datasets, the **application may occasionally hit memory limits** and restarts. For the most **stable experience**, run the app locally.

## Update: Autocomplete Search and “Try Demo Recommendation” Button
**Why did the system require changes?**

To **address usability limitations** and **improve the demo experience** for first-time users.
In the original version, users were required to browse Dataset A to know valid inputs and *manually* input the exact spelling of a song and artist from it. Specifically first-time users may have got confused. 

**What changes were implemented?**

The system was enhanced with two major features:
1. **Autocomplete Search**
   
   An autocomplete search **dynamically suggests** valid song–artist pairs from Dataset A as the user types, removing the need to manually search through the full dataset.
   
   The autocomplete **logic** works as follows: It queries Dataset A while the user types -> returns unique song–artist pairs -> automatically fills both fields when selected

3. **“Try Demo Recommendation” Button**
   
   This button allows users to instantly explore the recommender without typing anything based on "Help!" by the Beatles.
   
   When clicked, the button auto-fills a valid song–artist pair, applies predefined filters, and sends the recommendation request.

## App Screenshots (Updated Version)

### App with new features: Autocomplete Search and "Try demo recommendations" button
<img width="600" height="600" alt="Music_Recommender_App_New_Version" src="https://github.com/user-attachments/assets/d55d4aa1-2ced-4622-9b80-e003e63585d3" />

### Autocomplete Search in Action
<img width="600" height="600" alt="Music_Recommender_App_Autocomplete_in_Action" src="https://github.com/user-attachments/assets/31c4284a-03d6-4e57-8b36-d729586f1026" />

### Recommendations (based on Beautiful by Mariah Carey) Suggested by the App
<img width="600" height="600" alt="Music_Recommender_App_Suggested_Recommendations" src="https://github.com/user-attachments/assets/6bec44ce-7e4f-4802-850e-699df7559c84" />

## App Installation and Setup

This project requires two datasets. While originally public, they were preprocessed to ensure audio feature vectors are correctly formatted for cosine similarity computation.

1. Download the Datasets

Please download the following datasets and save them in .csv format:

- [Dataset A](https://drive.google.com/file/d/1Akz2p3eXFY-FGYoRKJk-g_hP1cZ1Rz84/view?usp=drive_link)

  It is used for selecting the song which sound (audio features) serves as the basis for personal recommendations.

- [Dataset B](https://drive.google.com/file/d/1_YFcLwIcb9GcTre4NkB_sSo4U4vZlyEG/view?usp=drive_link)

  It is the recommendation catalogue for fairness and diversity.

2. Link the Datasets to the Application
     
- Open ``` recommender.py ```

- Find 
  ``` # Loading datasets
      dataset_a_df = get_dataset(
        local_path = 'C:/Users/.../data/Dataset_A.csv',
        file_id ='1Akz2p3eXFY-FGYoRKJk-g_hP1cZ1Rz84', 
        encoding='latin-1', 
        delimiter=';'
      )
  ```

- Paste the full file path to Dataset_A.csv and Dataset_B.csv on your computer.
    
3. Run the Appplication
   
   Run ``` app.py ```, go to the generated URL, and start exploring fair and diverse music recommendations! :blush:

