class computer:
    def __init__(self):
        self.name='"Kshitij"'
        self.age=21
    def update(self):
        self.name='"Ritesh"'
        self.age=24
    def compare(self,other):
        if self.age==other.age and self.name==other.name:
            return True
        else:
            return False
c1=computer()
c1.update()
c2=computer()

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)