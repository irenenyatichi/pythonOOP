class Dog:
    def __init__(self,name,color,size):
        self.name = name
        self.color = color
        self.size = size
    def bark(self):
        return f"{self.name}, the dog, who is {self.color} in color is {self.size} in size but has a {self.bark} bark."
    def whine(self):
        return f"{self.name}, the dog, who is {self.color} in color, is {self.size} in size but likes to {self.whine} in a sad voice."