pos=-1
def search(list,n):
    l=0
    u=len(list)-1

    while l<=u:
        mid=(l+u)//2

        if list[mid]==n:
            globals()["pos"]=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1

    return False

list=[2,4,7,9,56,78,89,95,106,203,305]
n=106

if search(list,n):
    print("found at",pos+1)
else:
    print("Not found")

# Binary Search