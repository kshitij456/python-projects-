a=int(input("enter a no. \n"))
b=eval(input("enter the 2nd no. \n"))

try:
    print('"resource opened"')
    print(a/b)

except ZeroDivisionError as e:
    print("hey,you can't divide a no. by zero \n",e)
except ValueError as e:
    print("invalid input")
except Exception as e:
    print("something went wrong...")
finally:
    print('"resource closed"')
    print("Bye")
