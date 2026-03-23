class Book: 
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def hienthithongtin(self):
        return self.title + " - " + self.author + " (" + str(self.year) + ")"
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("Đắc nhân tâm", "Đặng Thùy Trâm", 2007)
print(book1.hienthithongtin())
print(book2.hienthithongtin())



class BankAccount:
    def __init__(self, account_number, balance = 0):
        self.__account_number = account_number
        self.balance = balance
    def get_account_number(self):
        return self.__account_number
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Số dư không đủ để rút tiền.")
    def get_balance(self):
        return "Số dư hiện tại: " + str(self.balance)
    
account1 = BankAccount("123456789")
print(account1.get_balance())
account1.deposit(500)
print(account1.get_balance())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def study(self):
        return self.name + " đang học bài."
    
student1 = Student("Alice", 20, "S12345")
print(student1.study())


class Vehicle:
    def __init__(self, make, model, brand):
        self.make = make
        self.model = model
        self.brand = brand
 
class Car(Vehicle):
    def __init__(self, make, model, brand, num_doors):
        super().__init__(make, model, brand)
        self.num_doors = num_doors

class Bike(Vehicle):
    def __init__(self, make, model, brand, type):
        super().__init__(make, model, brand)
        self.type = type
    def display_info(self):
        return f"Xe đạp {self.make} {self.model} của hãng {self.brand} là loại {self.type}."
    
bike1 = Bike("Giant", "Escape 3", "Giant", "Đường phố")
print(bike1.display_info())