#cannot leave empty
while True:
    name = input("Enter your name: ")
    if name !="":
        break
    
phone_number = "123_456_798"
for i in phone_number:
    if i == "_":
        continue
    print (i,end="")
    
    
for j in range (1,11):
    if j == 3:
        pass
    else:
        print (j)