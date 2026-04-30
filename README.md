# Music Recommender System  With Filters For Fairness & Diversity
This is a **content-based** music recommender system with user-controlled filters promoting **fairness** and **diversity**.

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
<img width="944" height="477" alt="App_Showing_Recommendations" src="https://github.com/user-attachments/assets/5c5845e6-a2bc-433d-8b9b-142a3c40b6a6" />

### App showing a message notifying that no songs matched the applied filters
<img width="953" height="481" alt="App_Showing_No_Matches_Found" src="https://github.com/user-attachments/assets/8131b62c-e893-4d5c-89c6-d473db999a98" />

## System Architecture
<img width="2013" height="1113" alt="MRS_Architecture" src="https://github.com/user-attachments/assets/d79ee697-3475-40a8-ac03-76b9bd0360b5" />

## Deployment and Hosting
This application was originally designed and hosted on Render using their Free Tier plan. While this provided a great entry point, the environment's limited RAM (512MB) proved insufficient for the app's processing needs. Because this project handles a large volume of data, the free cloud resources often lead to memory overflows. For the most **stable experience**, run the app locally.

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
<img width="1887" height="957" alt="Music_Recommender_App_New_Version" src="https://github.com/user-attachments/assets/5b27c18e-9118-4c11-b978-0886fd9688ae" />

### Autocomplete Search in Action
<img width="1885" height="957" alt="Music_Recommender_App_Autocomplete" src="https://github.com/user-attachments/assets/a0e270a9-eee5-47ca-b67b-e25818e181c5" />

### Recommendations (based on Beautiful by Mariah Carey) Suggested by the App
<img width="1875" height="951" alt="Music_Recommender_App_New_Version_Suggested_Recommendations" src="https://github.com/user-attachments/assets/1474be7d-2977-4f3a-8df5-384b9d6b618c" />

## Video Walkthrough
To get a feel for the interface and core features without setting everything up immediately, you can watch a short [video demonstration](https://drive.google.com/file/d/1qDwTwrSmxV7Bkvjxlf56fFfiCoozfscQ/view?usp=drive_link).

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

