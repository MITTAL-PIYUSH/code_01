n = int(input("Enter no. of Elements : "))
f,s = 1,1
for i in range(n):
    print(f,end = ' ')    #Print a statement
    t = f+s
    f = s
    s = t
