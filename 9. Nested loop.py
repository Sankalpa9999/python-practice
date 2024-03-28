rows = int(input("Enter number of rows: "))
column = int(input("Enter number of column: "))
symbol = input("Enter a symbol: ")
for i in range (rows):
    for j in range (column):
        print (symbol,end=" ")
    print()