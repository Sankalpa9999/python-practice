#scope


name = "Sankalpa" #global scope

def display_name():
    name = "Ojha"   #local scope
    print(name)
    
display_name()
print (name)