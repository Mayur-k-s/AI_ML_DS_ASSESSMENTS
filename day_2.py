#Section 1: Functions and OOP Concepts 

#1. 1. Case Study: Grocery Store Billing 
'''A grocery store wants to automate billing. 
Create a function to calculate the total bill amount for a list of items with their prices and quantities. 
'''
#solution
def totals_bill(n,list):
    for i in range(n):
        key= input("enter the item:")
        value=float(input("enter the price:"))
        quantity=float(input("enter the quantity:"))
        list[key]=[value,quantity]
    total_bill=0
    print("item         quantity    price/quantity    price ")
    for key in list:
        print(f"{key}            {list[key][1]}            {list[key][0]}            {list[key][0]*list[key][1]}")
        total_bill+=list[key][0]*list[key][1]
    return total_bill

print("enter the total no of items:",end="")
n=int(input())
list={}
print(f"total bill : {totals_bill(n,list)} rupees")

#2. 2. Case Study: School Report Generator 
'''A school wants to generate student reports using a function. 
Write a function that takes  student name, 
marks in 3 subjects and returns the average marks and grade. 
'''
#solution
def report(student_name,s1,s2,s3):
    average=int(s1+s2+s3)/3
    grade="f"
    if(average>90):
        grade="A"
        return average,grade
    elif (average>80):
        grade="B"
        return average,grade
    elif (average>70):
        grade="C"
        return average,grade
    

print("enter student name: ",end="")
student_name=input()
print("enter marks in 3 subs: ",end="")
s1=int(input())
s2=int(input())
s3=int(input())
print(f"the average marks and grade are:{report(student_name,s1,s2,s3)}")

#3. 3. Case Study: Temperature Converter 
'''Create a Python program using a function that converts temperature 
from Celsius to  Fahrenheit and vice versa based on user choice. 
'''
#solution

def converter(c):
    f=(c*(9/5))+32
    return f
print("enter the celsius temperature: ",end="")
c=int(input())
print(f"result in fahrenheit: {converter(c)}")

#4. 4. Case Study: Employee Management System 
'''An organization wants to create a simple employee management system.
 Design a class  Employee with attributes like name, ID, and salary.
Add a method to display the details.
'''
#solution
class empolyee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
print("enter employee name:",end="")
n=input()
print("id:",end="")
i=input()
print("salary:",end="")
s=input()
obj=empolyee(n,i,s)
print(obj.name)
print(obj.id)
print(obj.salary)


 #5. 5. Case Study: Bank Account Simulation 
'''
Write a class BankAccount that allows a user to deposit, withdraw, and check balance.
Use functions for each operation. 
'''
#solution
class bankaccount:
    def __init__(self,account_number,amt):
        self.account_number=account_number
        self.amt=amt
    def d(self,deposit):
        self.amt=self.amt+deposit
        return self.amt
    def w(self,withdraw):
        self.amt=self.amt-withdraw
        return self.amt
    def b(self):
        return self.amt

print("enter account number:",end="")
a=input() 
print("enter amount:",end="")
am=int(input())
obj=bankaccount(a,am)
print(f"account_number:{obj.account_number}")
print(f"amount:{obj.amt}")
print(f"deposit:{obj.d(10000)}")
print(f"withdraw:{obj.w(5000)}")
print(f"balance:{obj.b()}")


#6. 6. Case Study: Movie Ticket Booking System 
'''Design a class MovieTicket with attributes like movie name, seat number, and price.
  Include a method to calculate total price for multiple tickets.
  '''
#solution
class movieticket:
    def __init__(self,name,seat,price):
        self.name=name
        self.seat=seat
        self.price=price
        self.n=n
    def total_price(self,qty):
        qty=qty*self.price
        return qty
print("enter movie name:",end="")
m=input()
print("enter how many tickects:",end="")
n=int(input())
print("enter the price: ",end="")
p=float(input())
print("enter seat no:",end="")
s=input()
obj=movieticket(m,s,p)
print(f"name:{obj.name}")
print(f"seat:{obj.seat}")
print(f"price:{obj.price}")
print(f"total price:{obj.total_price(n)}")

    
#7. 7. Case Study: Library Book Management 
'''A library wants to keep track of books.
 Create a class Book with attributes like title,  author, and availability.
   Include methods to borrow and return a book.
'''
#solution
class book:
    def __init__(self,title,author,availability):
        self.title=title
        self.author=author
        self.availability=availability
    
    def borrow(self,b):
        if(b==self.title and self.availability>0):
            self.availability=self.availability-1
            print("book borrowed for a week")
    def returning(self,b):
        self.availability=self.availability+1
        print("book returned")

    def avail(self):
       return self.availability

obj=book("verity","mayur",10)
print(obj.borrow("verity"))
print(obj.returning("verity"))
print(obj.avail())
    

#8. 8. Case Study: Car Rental System 
'''
Write a class Car with attributes like brand, model, and daily rent. 
Create a function to  calculate rent for a given number of days.
'''
#solution
class car:
    def __init__(self,b,m,r):
        self.b=b
        self.m=m
        self.r=r
    
    def total_rent(self,d):
        return (d*self.r)


    def display(self):
        print(f"brand:{self.b}")
        print(f"model:{self.m}")
        print(f"daily rent:{self.r}")
obj=car("mahendra","xuv700",1000)
print(obj.display())
print(obj.total_rent(8))

#9. 9. Case Study: Online Course Progress Tracker 
'''
Create a class Course with attributes course name, total modules, and completed  modules.
 Write a method to display the percentage of course completion
 '''
#solution

class course:
    def __init__(self,n,t_m,c_m):
        self.n=n
        self.t_m=t_m
        self.c_m=c_m
    
    def percentage(self):
        return ((self.c_m/self.t_m)*100)

    def display(self):
        print(f"course name:{self.n}")
        print(f"total modules:{self.t_m}")
        print(f"completed modules:{self.c_m}")
obj=course("python",20,10)
print(obj.display())
print(f"percentage of completion:{obj.percentage()}")

    
#10. 10. Case Study: Restaurant Order System 
'''
Design a function to accept a list of food items ordered and their prices,
 then return the  total bill amount and number of items ordered.
 '''

#solution
def total(order):
    total_item=0
    total_price=0
    for items,price in order:
        total_item+=1
        total_price+=price
    return total_price,total_item

order=[("apple",120),("orange",130),("banana",55)]
print(total(order))


 
