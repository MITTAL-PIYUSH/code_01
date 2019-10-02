# recursive function
def factorial(n):
    if n==1 :
        return 1

    f = n*factorial(n-1) # recursive statement
    return f 

n = int(input("Enter a number :"))               #To Take a input
print(f"Factorial of {n} : {factorial(n)}")
