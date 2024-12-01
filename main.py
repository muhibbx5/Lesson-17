try:
      num=int(input("Please enter a number : "))
      print("The number you entered is :",num)
except ValueError as ex:
      print("exception : ", ex)     