# CLEAR
class MyDict:
    def __init__(self):
        self.data = {}

    def clear(self):
        for key in list(self.data.keys()):
            del self.data[key]

d = MyDict()
d.data = {"a": 1, "b": 2, "c": 3}

d.clear()
print(d.data) 
