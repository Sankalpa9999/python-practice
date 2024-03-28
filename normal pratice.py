first_name = "Sankalpa"
print ("My name is",first_name,"Ojha")

x = "I am sorry!"
a = 0

while a<=5 :
    a = a+1
    print (a,end=". "+x)
    print()
    
for b in range(5,10):
    b = b + 1
    print (b,end=". "+x)
    print()

for i in range(5):
    print (x)
    
name = ["Ram", "Shyam", "Hari", "Bimal"]
name.sort()
for i in name:
    print (i)
    

age = int(input("Enter your age: "))

if age>= 18:
    print("You can apply for our service")
        
if age<=18:
    print (" sorry! You can't apply for our service")
        
if age>=50:
    print (" sorry! You can't apply for our service")
    
    
    
