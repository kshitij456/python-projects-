class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
        """lap1.show()"""

    class laptop:
        def __init__(self):
            self.brand="asus"
            self.cpu="i5"
            self.ram="8gb"

        def update(self):
            self.brand="lenovo"
            self.cpu="i7"
            self.ram="8gb"
            
        def show(self):
            print(self.brand,self.cpu,self.ram)
            
s1=student("kshitij",33)
s2=student("ritesh",34)
s2.lap.update()

"""  Object of inner class outside outer class 
lap1=student.laptop()
lap1.update()
"""

s1.show()
print()
s2.show()
