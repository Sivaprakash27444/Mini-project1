def nat(n):
    print("Natural number series: ")
    for i in range(1,n+1):
        print(i,end=" ")
    print()

def eve(n):
    print("Even numbers series: ")
    for i in range(2, n+1, 2):
        print(i,end=" ")
    print()

def odd(n):
    print("Odd number series: ")
    for i in range(1,n+1,2):
        print(i,end=" ")
    print()

def fib(n):
    print("Fibonnaci number: ")
    a, b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b

print("1=Natural Number")
print("2=Even number")
print("3= Odd NUmber")
print("4=Fibonnaci Number")

m=int(input("Enter number: "))
choice=int(input("Enter choice:"))

if choice==1:
    print("Natural Number",nat(m))
elif choice==2:
    print("Even number",eve(m))
elif choice==3:
    print("Odd Number",odd(m))
elif choice==4:
    print("Fibonnaci Number",fib(m))
else:
    print("Invalid Input")