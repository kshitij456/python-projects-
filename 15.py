class car:
    wheels="4W"
    def __init__(self):
        self.mileage="10kmpl"
        self.company='"BMW"'
c1=car()
c2=car()
c2.mileage="15kmpl"
c2.wheels="5W"
print(c1.mileage,c1.company,c1.wheels)
print(c2.mileage,c2.company,c2.wheels)
