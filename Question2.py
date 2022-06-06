list=[5,8,9,2,4,1,3,45,2,3,89,4,63,23,4,87,75,64,1]
new_list=[]

while list:
    min=list[0]
    for i in list:
        if i < min:
            min = i

    new_list.append(min)
    list.remove(min)

print(new_list)
new_list.reverse()   # Using reverse operator
print(new_list)

# Using reverse as a function
def rev(l):
    return l[::-1]
print(rev(new_list))

print(set(x for x in new_list if new_list.count(x) > 1))    # Print duplicates in a list

# Sorting using while loop