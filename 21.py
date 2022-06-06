class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        s=0
        if(a!=None and b!=None and c!=None):
            s=a+b+c
        elif(a!=None and b!=None):
            s=a+b
        elif(a!=None and c!=None):
            s=a+c
        elif (b!=None and c!=None):
            s=b+c
        else:
            s=a

        return s

    def __str__(self):
        return '({},{})'.format(self.m1,self.m2)
    
s1=student(34,89)
print(s1)
print(s1.sum(78,56,89))