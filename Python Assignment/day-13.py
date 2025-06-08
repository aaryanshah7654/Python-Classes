#Create a Book class with title, author, and a describe() method.
class book:
    def __init__(self, title, author):
        self.title = title      
        self.author = author    

    def describe(self):
        print(f"'{self.title}' is written by {self.author}.")

book_1 =book("Wings of Fire", "A.P.J. Abdul Kalam")
book_1.describe()

#Extend Book to EBook with a file_size attribute. (Inheritance)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"'{self.title}' by {self.author}")

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  
        self.file_size = file_size       

    def describe(self):
        print(f"'{self.title}' by {self.author} - File Size: {self.file_size}MB")

ebook1 = EBook("Python", "Aaryan", 50)
ebook1.describe()  

#Add a calculate_area() method to both Rectangle and Circle.  (Polymorphism)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(5, 4), Circle(3)]

for shape in shapes:
    print(shape.calculate_area())

#Modify BankAccount to prevent negative withdrawals. (Encapsulation)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:      
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Amount")

account = BankAccount(1000)
account.withdraw(500)
print(account.get_balance())

#Implement a Logger abstract class with FileLogger and ConsoleLogger subclasses.     ( Abstraction)
from abc import ABC, abstractmethod

class Logger(ABC):
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        print(f"Writing to file: {message}")

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"Console log: {message}")

logger1 = FileLogger()
logger1.log("File saved successfully!")

logger2 = ConsoleLogger()
logger2.log("User logged in.")

#Add __str__ to Playlist to display song count. (Magic Methods)
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __add__(self, other):
        return Playlist(self.songs + other.songs)

    def __str__(self):
        return f"Playlist with {len(self)} songs"

rock = Playlist(["Song A", "Song B"])
lofi = Playlist(["Song C", "Song D", "Song E"])

print(len(rock))         
print(rock)            

combined = rock + lofi
print(combined)          
