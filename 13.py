class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config is",self.cpu,self.ram)
c1=computer("i5","8GB")
c2=computer("i7","16GB")
c1.config()
c2.config()