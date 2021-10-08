import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv("filtered_stars.csv")
df.head()
df.columns
df.drop(['Unnamed: 0', 'Unnamed: 0.1'],axis=1,inplace=True)
name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()
plt.figure(figsize=(10,5))
plt.title("Stars Solar Mass")
plt.bar(name[0:9],mass[0:9])
plt.figure(figsize=(10,5))
plt.title("Stars Solar Radius")
plt.bar(name[0:9],radius[0:9])
plt.figure(figsize=(10,5))
plt.title("Stars Gravity(m/s^2)")
plt.bar(name[0:9],gravity[0:9])
plt.figure(figsize=(10,5))
plt.title("Stars Gravity(m/s^2)")
plt.bar(name[0:9],dist[0:9])
