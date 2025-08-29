import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

# importing data
df = pd.read_csv("dataset/tracks.csv")
print(f"Dataset shape: {df.shape}")
df.head()

# EDA
df.info()
df.describe()
print(df.isnull().sum()) # Check missing values

# Correlation heatmap
audio_features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
plt.figure(figsize=(12, 8))
correlation_matrix = df[audio_features + ['popularity']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Feature Correlation Matrix')
plt.show()
correlations = df[audio_features].corrwith(df['popularity']).sort_values(ascending=False)
print("Feature correlations with popularity:")
print(correlations)