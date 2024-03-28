#Dictionary
capitals = {"Nepal":"kathmandu",
            "India":"New Dehli",
            "China":"Beijing",
            "Russia":"Moscow"}
capitals.update({"Germany":"Berlin"})
capitals.pop("India")
capitals.update({"Nepal":"Pokhara"})
#capitals.clear()

print (capitals["Germany"])
print (capitals.get("Germany"))
print (capitals.keys())
print (capitals.values())
print (capitals.items())

for key,value in capitals.items():
    print (key,end=" : "+value)
    print()