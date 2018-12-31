# Capstone_Project2

## MLB Pitching

This repository contains all files relevant to my second capstone project as part of Springboard's Data Science Career Track mentorship program.

The goal of this project is to develop a model that could reliably predict the outcome of a pitch given factors about what the pitcher wants to throw. The hopes for this model is to utilized by pitchers and coaches/managers to take those factors to effectively predict the outcome of the pitch which  will hopefully lead to more effective pitching and lower pitch counts. If you'd like to find out more behind the motivation of this project, it could be found in the Capstone Project 2 Proposal document above.

This repository is laid out in the following structure:
- get_data
  - get_data.py
    - This file extracts JSON data of all plays of all regular season games played from 2015-2017 and saves it in another JSON file
- Data_Wrangling
  - Data_Wrangling.ipynb
    - Notebook containing all necessary cleaning and feature engineering
  - Data_Wrangling.py
    - Python script of same code in Data_Wrangling.ipynb
  - get_pitches_data.py
    - This file defines a function to extract all necessary data regarding pitches and their outcomes for this project
  - json_to_csv.py
    - Script that utilizes the function written in get_pitches_data.py and the data extracted from get_data.py and saves it as a CSV
- EDA
  - Exploratory_Data_Analysis.ipynb
    - Notebook exploring any patterns within the data
-Machine_Learning
  - (A number of folders containing machine learning models and train history visualizations)
  - Machine_Learning_Models.ipynb
    - Notebook of baseline, untuned models, one of which would be futher tuned
  - model_calls_id.ipynb
    - Futher tuning of the model chosen from Machine_Learning_Models.ipynb
  - model_metrics.csv
    - A CSV file used to compare different model metrics with each other
- Final
  - Capstone_Project2_Milestone_Report.pdf
    - Report summarizing the steps taken up to Exploratory Data Analysis
  - Capstone_Project2_Milestone_Report2.pdf
    - A second report regarding processes and issues during machine learning development
  - Capstone_Project2_Presentation.ipynb
    - Notebook used to present the project
  - Capstone_Project2_Presentation.slides.html
    - Actual slideshow of the presentation
