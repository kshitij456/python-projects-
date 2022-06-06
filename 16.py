class student:
    university="CSVTU"
    def __init__(self,m1,m2,m3,name):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.name=name
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    @classmethod
    def info(cls):
       return cls.university
    @staticmethod
    def getuniversity():
        print("IIT")
    def details(self):
        print("Name:",self.name)
        print("Maths:",self.m1,"\t\tPhysics:",self.m2,"\tChemistry:",self.m3)
s1=student(34,89,67,"Kshitij")
s2=student(56,98,23,"Sudhanshu")
print(s1.avg())
s1.details()
print(student.info())
print()
print(s2.avg())
s2.details()
student.getuniversity()
