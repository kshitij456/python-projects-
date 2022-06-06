from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(2):
            print("Hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(2):
            print("Hi")
            sleep(1)

class I(Thread):
    def run(self):
        for i in range(2):
            print("I")
            sleep(1)

class Am(Thread):
    def run(self):
        for i in range(2):
            print("Am")
            sleep(1)

class Kshitij(Thread):
    def run(self):
        for i in range(2):
            print("Kshitij")
            sleep(1)

t1=Hello()
t2=Hi()
t3=I()
t4=Am()
t5=Kshitij()

t1.start()
sleep(0.2)
t2.start()
sleep(0.2)
t3.start()
sleep(0.2)
t4.start()
sleep(0.2)
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

print("\n")
print('"Bye"')