class myClass():
    def __init__(self):
        self.user_string = ""
    
    def getString(self):
        self.user_string = input("Enter a string: ")
    
    def printString(self):
        if self.user_string: 
            print(self.user_string.upper())
        else:
            print("No string to print.")

processor = myClass()
processor.getString() 
processor.printString() 

#2
class Shape:
    def __init__(self):
        self.area_value = 0

    def area(self):
        print(f"Area: {self.area_value}")


class Square(Shape):
    def __init__(self, length):
        super().__init__()  
        self.length = length
        self.area_value = self.length ** 2 

    def area(self):
        """Print the area of the square."""
        print(f"Area of Square: {self.area_value}")

shape = Shape()
shape.area()  
square = Square(5)
square.area()  

#3
class Shape:
    def __init__(self):

        self.area_value = 0

    def area(self):
        print(f"Area: {self.area_value}")


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__() 
        self.length = length
        self.width = width
        self.area_value = self.length * self.width  
    def area(self):
        print(f"Area of Rectangle: {self.area_value}")

shape = Shape()
shape.area()  

rectangle = Rectangle(5, 3)
rectangle.area()

#4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"Point moved to: ({self.x}, {self.y})")
    
    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance


point1 = Point(3, 4)
point1.show()  

point2 = Point(6, 8)
point2.show()  

point1.move(2, 3) 

distance = point1.dist(point2)
print(f"Distance between point1 and point2: {distance}")

#5
class Account:
    def __init__(self, owner, balance=0):

        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
    
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
       
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds! ")
        else:
            print("Withdrawal amount must be positive.")

account = Account("John", 100)

account.deposit(50)  
account.withdraw(30)  
account.withdraw(150)  
account.deposit(200)  
account.withdraw(100)  

print(f"Final balance for {account.owner}: {account.balance}")

#6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = int(input)

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)



