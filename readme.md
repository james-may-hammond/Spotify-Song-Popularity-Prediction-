# Spotify-Song-Popularity-Prediction

## Objectives
- To make and deploy regression model to predict song popularity based on audio features.


## EDA - Exploratory Data Analysis
- *What is EDA?* =>
  - EDA is the process of exploring or getting to know the dataset we're working with
  - Our main incentive is to
    - Detect patterns & outliers
    - Data cleaning
    - Visualisation
- *Correlation Heatmap* =>
  - It is a plot that highlights the corellation of one feature from another feauture
  - So for example:
    - Energy vs dancability = 0.24
    - Acousticness vs dancability = -0.24
    - This is as per out heatmap and we can conclude that energeti songs are more danceable than acoustic songs which is trivial.
    ![[plots/correlation_matrix.png]]
