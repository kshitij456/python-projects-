class PyCharm():
    def execute(self):
        print("compiling")
        print("running")
class MyEditor():
    def execute(self):
        print("compiling")
        print("running")
        print("spell checking")
        print("convention checking")
class laptop():
    def code(self,ide):
        ide.execute()
ide=MyEditor()
lap1=laptop()
print('"In MyEditor"')
lap1.code(ide)
print('"In PyCharm"')
ide=PyCharm()
lap1.code(ide)
