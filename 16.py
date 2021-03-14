class student:
    school="CSVTU"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    @classmethod
    def info(cls):
       return cls.school
    @staticmethod
    def getschool():
        print("IIT")
s1=student(34,89,67)
s2=student(56,98,23)
print(s1.avg())
print(s2.avg())
print(student.info())
student.getschool()