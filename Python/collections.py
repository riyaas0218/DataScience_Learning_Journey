#set unordered and mutable

uber_city={"Chennai","Banglore","Mumbai","Coachi"}
uber_city2={"Chennai","Hydrabad","Coachi","Sivaganga"}

print(uber_city.union(uber_city2))
print(uber_city.intersection(uber_city2))
print(uber_city2.difference(uber_city))

my_set={1,2,3,5}
my_set.discard(8)  # for safe deletion it avoid error wher delete element no in set



#Dictionary Collection


my_datails={
    "Name" : "Riyas",
    "Age" : 22,
    "City" : "Chennai",
    "Desgination" :"Data Scientist",
    "Last_Name" :"Ajmal Khan"
}

print(my_datails["Age"])
#print(my_details["Chennai"]) it show error it not a safe method only using key for get value

print(my_datails.get("Desgination"))
print(my_datails.keys())
print(my_datails.values())



my_datails.update({"Mother_Name": "Subira Banu"})  #update did upset means if it there already update the value if not add what we give
for key,val in my_datails.items():
    print(f"{key} : {val}")       
                                  
                                  