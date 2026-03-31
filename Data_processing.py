import pandas as pd
import googlemaps
import time

df = pd.read_csv("D:\office\Projects\python\simumilk extra\datasimu.csv") 
locations = list(zip(df["Latitude"], df["Longitude"]))
names = df["Name"].tolist()

API_KEY = "AIzaSyBYmyTuPmWaPHIGMaigf557UiSSF0pFPvA"
gmaps = googlemaps.Client(key=API_KEY)

distance_matrix_km = []

for i in range(len(locations)):
    origin = [locations[i]]
    matrix = gmaps.distance_matrix(origins=origin,
                                   destinations=locations,
                                   mode="driving",
                                   units="metric")

    row_km = []
    for element in matrix["rows"][0]["elements"]:
        if element["status"] == "OK":
            km = element["distance"]["value"] / 1000  # m to km
        else:
            km = None
        row_km.append(km)

    distance_matrix_km.append(row_km)
    time.sleep(1) 


df_result = pd.DataFrame(distance_matrix_km, index=names, columns=names)
df_result.to_excel("distance_matrix.xlsx")
print("distance_matrix.xlsx")
