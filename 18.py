class A:
    def __init__(self):
        print('"IN A"')
        
    def feature1(self):
        print("feature1 is working")
        
    def feature2(self):
        print("feature2 is working")
        
class B(A):
    def __init__(self):
        super().__init__()
        print('"IN B"')
        
    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is working")
class C(B):
    def __init__(self):
        super().__init__()
        print('"IN C"')
        
    def feature5(self):
        print("feature5 is working")
a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()