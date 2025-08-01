# %%
import pandas as pd
from geopy.geocoders import Nominatim 
# %%
df = pd.read_csv('supermarkets.csv')
df
# %%
nom = Nominatim(user_agent="my-application-name", timeout=10)
# %%
df['Address'] = df['Address'] + ', '+ df['City'] + ', '+ df['State'] + ', '+ df['Country'] 
# %%
df
# %%
df['Coordenadas'] = df['Address'].apply(nom.geocode)
# %%
df
# %%
df['Latitud'] = df['Coordenadas'].apply(lambda x: x.latitude if x != None else None)
df 
# %%
df['Longitud'] = df['Coordenadas'].apply(lambda x: x.longitude if x != None else None)
# %%
df
# %%
nom.geocode('Carrera 7H #42-104, Barranquilla, Colombia')
# %%
