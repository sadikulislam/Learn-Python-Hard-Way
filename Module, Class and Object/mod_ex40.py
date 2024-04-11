import ex40

ex40.apple()
print(ex40.orange)

class MyStuff(object):
    def __init__(self):
        self.tangerine = "Very tasty"

    def apple(self):
        print("I am apple from class.")

thing = MyStuff()

thing.apple()
print(thing.tangerine)