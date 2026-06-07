class Var:
"""
A counter class that you can add to your variables.
Just write (any variable) = Var(value) and you never have to write the equals sign for your variables! (only if its adding, subtracting, multiplying, dividing)
To get the value, use (your variable).value or just add the class Var because this class has a __str__ dunder method.
"""
    def __init__(self, value: any):
        self.value = value
    def __str__(self):
        return self.value
    def add(self, anyval: any):
        self.value += anyval
    def subtract(self, anyval: any):
        self.value -= anyval
    def multiply(self, anyval: any):
        self.value *= anyval
    def divide(self, anyval: any):
        self.value += anyval
