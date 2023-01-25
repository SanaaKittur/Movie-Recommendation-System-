import numpy as np
import pandas as pd
import plotly.express as px

print("--> MOVIE DETAILS","\n")

movies = pd.read_csv("/content/media/movies/movies.dat", delimiter='::', engine="python")
print(movies.head(),"\n")

print("--> SPECIFYING COLUMN NAMES","\n")

movies.columns = ["ID", "Title", "Genre"]
print(movies.head(),"\n")

print("--> MOVIE RATING DETAILS","\n")

ratings = pd.read_csv("/content/media/movies/ratings.dat", delimiter='::', engine="python")
print(ratings.head(),"\n")

print("--> SPECIFYING COLUMN NAMES","\n")

ratings.columns = ["User", "ID", "Ratings", "Timestamp"]
print(ratings.head(),"\n")

print("--> THE FINAL MERGED TABLE","\n")

data = pd.merge(movies, ratings, on=["ID", "ID"])
print(data.head(),"\n")

ratings = data["Ratings"].value_counts()
numbers = ratings.index
quantity = ratings.values

fig = px.pie(data, values=quantity, names=numbers)
print("--> GRAPH SHOWING RATINGS DISTRIBUTION","\n")

fig.show()

print("--> THE MOVIES LISTED BELOW ARE A MUST WATCH","\n")

data2 = data.query("Ratings == 10")
print(data2["Title"].value_counts().head(10))
