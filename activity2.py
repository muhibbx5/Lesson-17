try:
     num1,num2=eval(input("Enter 2 number seperated by commas (e.g 200,200) : "))
     result=num1/num2
     print("The result is :", result)
except ZeroDivisionError:
     print("Division by zero is always an error!!!")
except SyntaxError:
     print("The comma is missing enter a number and seperate it with comma (e.g 200,200)")
except:
     print("WRONG INPUT!!")
else:
     print("NO EXCEPTIONS.")
finally:
     print("It will excute it doesn't matter.")