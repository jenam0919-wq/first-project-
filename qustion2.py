# class calculator:
#     def __init__(self,n):
#         self.n=n

#     def squre(self):
#         print(f"the squre is{self.n*self.n}")

#     def cube(self):
#         print(f"the cube is {self.n*self.n*self.n}")

#     def root(self):
#         print(f"the root is {self.n**1/2}")
#     @staticmethod
#     def hello():
#         print("ok nice!")

# a=calculator(45)
# a.hello
# a.squre
# a.cube
# a.root

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")

    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def root(self):
        print(f"The root is {self.n ** 0.5}")

    @staticmethod
    def hello():
        print("ok nice!")


a = Calculator(45)
a.hello()
a.square()
a.cube()
a.root()
