class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def test(self):
        print("hello there " + self.name)