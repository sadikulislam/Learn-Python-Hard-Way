class Parent(object):
    def impicit(self):
        print("Parent impicit.")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.impicit()
son.impicit()