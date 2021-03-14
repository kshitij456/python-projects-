a=5
b=0
try:
    print('"resource opened"')
    print(a/b)
    k=int(input("enter a no. \n"))
    print(k)

except ZeroDivisionError as e:
    print("hey,you can't divide a no. by zero \n",e)
except ValueError as e:
    print("invalid input")
except Exception as e:
    print("something went wrong...")
finally:
    print('"resource closed"')
    print("Bye")
