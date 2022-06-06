i=2
print("3 is prime")
while i<1000:
    j=2
    while(j<=(i/j)):
        if not(i%j):
            break
        j=j+1
        if(j>(i/j)):
            print(i,"is prime")
    i=i+1

