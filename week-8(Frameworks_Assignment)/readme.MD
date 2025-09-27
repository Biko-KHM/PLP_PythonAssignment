CORD-19 Data Analysis and Streamlit App
Assignment Overview
This assignment analyzes the CORD-19 dataset (metadata.csv) using Python, focusing on COVID-19 research papers. It includes data exploration, cleaning, visualization, and a Streamlit web app to display findings.
Learning Objectives

Load and explore real-world datasets
Apply basic data cleaning techniques
Create meaningful visualizations
Build an interactive Streamlit application
Present data insights effectively

Dataset

Source: Kaggle (CORD-19 Research Challenge)
File: metadata.csv (titles, abstracts, publication dates, authors, journals, sources)
Note: Due to the large size of the original file, a sample of specific rows is used for this project to enable GitHub compatibility.

Tools

Python 3.7+
Libraries: pandas, matplotlib, seaborn, wordcloud, streamlit
Environment: Virtual environment (.venv)

Project Structure

week-8(Frameworks_Assignment)/app.py: Streamlit app with visualizations
analysis.py: Data analysis script
publications_by_year.png, title_wordcloud.png, etc.: Generated visualizations
requirements.txt: Dependency list
README.md: This file

Tasks Completed

Data Loading: Loaded a sample of metadata.csv into a pandas DataFrame.
Exploration: Checked dimensions, data types, missing values, and basic stats.
Cleaning: Handled missing data, converted dates, added abstract word count.
Analysis: Counted papers by year, identified top journals, analyzed title words.
Visualizations: Plotted publications over time, top journals, source distribution, and title word cloud.
Streamlit App: Built an interactive app with title, sliders, and visualizations.
Documentation: Added comments and this README.

How to Run

Navigate to week-8(Frameworks_Assignment):cd week-8\(Frameworks_Assignment\)


Activate virtual environment:source .venv/Scripts/activate


Install dependencies:pip install -r ../../requirements.txt


Run the app:streamlit run app.py



Reflections

Challenges: Handling large dataset size led to using a sample; debugging missing dependencies.
Learning: Gained experience with pandas, visualization libraries, and Streamlit deployment.