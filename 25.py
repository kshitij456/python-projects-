f=open('kshitij','r')

f1=open('data','a')

for data in f:
    f1.write(data)

f1.write("\n BYe\n")
f1.write("Something\n")

print(f)
print(f.readline())
print(f.readline())
print(f.readline())



