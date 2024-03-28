temp = int(input("Enter the tmeperature: "))

if temp >=0 and temp <=9:
    print ("Temperature is little cold today.")
    
    
elif temp >=10 and temp <=30:
    print("The temperature is good today.")
    
    
elif temp <1 and temp > -30:
    print("Temperature is very clod today.")
    
    
elif temp <=0 and temp >=9:
    print ("Temperature is little cold today.")
    
    
elif temp >30:
    print ("Its very hot Today")
    
    
else:
    print("Its very bad.")