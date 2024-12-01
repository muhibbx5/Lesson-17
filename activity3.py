valid=False
while not valid:
 try:
    n=int(input("Please enter a number : "))
    while n%2==0:
     print("bye")
    valid=True
 except ValueError:
     print("It's invalid")

