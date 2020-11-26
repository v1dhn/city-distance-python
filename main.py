# Replace the text in key with your API Key
from geopy import distance
from opencage.geocoder import OpenCageGeocode
import pandas as pd

fileName = "test.xlsx"

key = 'Insert Your API Key here'

data = OpenCageGeocode(key)
n = int(input("How many inputs: "))
l = [] 
c1=[]
c2=[]
dist=[]
for i in range(n):
    query1,query2 = input().split()
    result1 = data.geocode(query1)
    result2 = data.geocode(query2)
    c1.append(query1)
    c2.append(query2)
    pos1 = result1[0]['geometry']['lat'] , result1[0]['geometry']['lng']
    pos2 = result2[0]['geometry']['lat'] , result2[0]['geometry']['lng']
    l.append((pos1,pos2))

for pos in l:
    pos1 = pos[0]
    pos2 = pos[1]
    dist.append(str(round(distance.distance(pos1,pos2).km,1))+"km")
datatemp = {"City1":c1,"City2":c2,"Distance":dist}
table = pd.DataFrame(datatemp)
table.to_excel(fileName)
print(table)
