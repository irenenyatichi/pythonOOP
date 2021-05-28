class Dog:
    def __init__(self,name,color,size):
        self.name = name
        self.color = color
        self.size = size
    def bark(self):
        return f"{self.name}, the dog, is color {self.color} and very {self.size} in size."
    def whine(self):
        return f"{self.name}, the dog, is color {self.color} and very {self.size} in size."
