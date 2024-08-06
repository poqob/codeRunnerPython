# File: src/packageA/a.py
#a.py
class A:
    def methodA(self):
        pass
    

# File: src/packageB/b.py
#b.py
class B:
    def methodB(self):
        pass


# File: src/packageC/c.py
#c.py
# a.py
class C:
    def methodC(self):
        pass


# File: src/main.py
#author: poqob
#date: 04.08.24
#Code Runner


class Main:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def run(self):
        pass


if __name__=='__main__':
    main = Main()
    main.run()
    main.__del__()

