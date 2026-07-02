

fav_cities=[]
for i in range(1, 5):
    print("Enter your fav city at position", i,":")
    str=input()
    fav_cities.append(str)
for i in range(len(fav_cities)-1,-1,-1):
    print("My fav city at position", i,"is", fav_cities[i])