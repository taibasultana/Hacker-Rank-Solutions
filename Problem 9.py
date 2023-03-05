#Pattern Program

n=int(input("Enter the numbers of row:"))
for i in range (1,n+1):
    for j in range (1, i+1):
        print (j, end="")
    print()
    