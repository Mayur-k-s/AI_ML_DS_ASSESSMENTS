#1. Case Study: Grocery Billing System
''' 
    Problem: A shopkeeper wants to generate a total bill using item prices.
    Task: Take a list of prices and compute the total using a loop.
    Test Case:
    Input: [50, 20, 30, 100]
    Output: Total Bill: 200 
'''
#solution
print("enter the total no of items:",end="")
n=int(input())
list={}
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
print(f"total bill : {total_bill} rupees")

#2. Case Study: Student Grades
'''
Problem: Calculate the average marks of a student using a tuple of 5 subjects.
Test Case:
Input: (80, 90, 70, 60, 85)
Output: Average: 77.0
'''
#solution
print("enter the no of students:",end="")
n=int(input())
print("enter the no of subjects:",end="")
s=int(input())
data={}
for i in range(n):
    print(f"enter name of student {i+1}:")
    key=input()
    value=()
    average_marks=0
    for j in range(s):
        value=list(value)
        print(f"enter subject {j+1} marks:")
        m=int(input())
        average_marks+=m
        value.append(m)
    value=tuple(value) 
    data[key]=[value,average_marks/s]
print(data)

          

#3. Case Study: Set of Unique Emails
'''
Problem: Extract unique email addresses from a list using a set.
Test Case:
Input: ['a@gmail.com', 'b@gmail.com', 'a@gmail.com']
Output: {'a@gmail.com', 'b@gmail.com'}
'''
data=[]
print("enter no of emails:")
n=int(input())
for i in range(n):
    print("enter email:")
    e=input()
    if("@gmail.com" in e):
        data.append(e)
print(data)
unique=set()
for i in data:
    unique.add(i)
print(unique)

#4. Case Study: Attendance Tracker
'''
Problem: Use a dictionary to store and print student names with their attendance status.
Test Case:
Input: {'Alice': 'Present', 'Bob': 'Absent'}
Output:
Alice: Present
Bob: Absent
'''
#solution
print("enter the no of students:",end="")
n=int(input())
data={}
for i in range(n):
    print("enter student name:",end="")
    key=input()
    print("enter p r a:",end="")
    value=input()
    if(value=='p' or value=='a'):
        data[key]=value
    else:
        continue
print(data)

#5. Case Study: Multiplication Table
'''
Problem: Print the multiplication table of a number using a loop.
Test Case:
Input: n = 4
Output: 4 8 12 16 20 24 28 32 36 40
'''
#solution
print("enter which multiplication table should be display:",end="")
n=int(input())
print("enter upto which ,the table should be display:",end="")
w=int(input())
for i in range(w):
    print(f"{i+1} * {n} = {(i+1) * n}")

#6. Case Study: Power Calculator
'''
Problem: Raise each number in a list to the power of 2 using a loop.
Test Case:
Input: [1, 2, 3]
Output: [1, 4, 9]
'''
#solution
print("enter the no of elements in the list:",end="")
n=int(input())
list=[]
for i in range(n):
    print(f"enter the element no {i+1}:",end="")
    e=int(input())
    list.append(e)
print(list)
power_list=[]
for i in list:
    power_list.append(i**2)
print(power_list)

#7. Case Study: Diamond Star Pattern
'''
Problem: A school wants to print a diamond pattern for decorations using `*`. Write a
program using nested loops to print a diamond star pattern of height n.
Note: The height will always be an odd number.
Test Case:
Input: n = 5
Output:
*
***
*****
***
*
'''
#solution
print("Enter the height (odd number): ", end="")
n = int(input())
if n % 2 == 0:
    print("Please enter an odd number.")
else:
    mid = n // 2  
    print(mid)
    for i in range(mid + 1):
        spaces = mid - i
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)
    for i in range(mid - 1, -1, -1):
        spaces = mid - i
        stars = 2 * i + 1
        print(" " * spaces + "*" * stars)

#8. Case Study: Count Even and Odd
'''
Problem: Count even and odd numbers from a tuple using a loop.
Test Case:
Input: (1, 2, 3, 4, 5)
Output: Even: 2, Odd: 3
'''
#solution
print("enter the no of element:",end="")
n=int(input())
t=()
even=0
odd=0
for i in range(n):
    t=list(t)
    e=int(input())
    t.append(e)
    t=tuple(t)
    if(e%2==0):
        even=even+1
    else:
        odd=odd+1
print(t)
print(f"even: {even}")
print(f"odd: {odd}")


#9. Case Study: Unique Fruits
'''
Problem: From a list of fruits, print the unique ones using set.
Test Case:
Input: ['apple', 'banana', 'apple', 'orange']
Output: {'apple', 'banana', 'orange'}
'''
#solution
print("enter no of fruits:",end="")
n=int(input())
l=[]
s=set()
for i in range(n):
    e=input()
    l.append(e)
print(l)
for i in l:
    s.add(i)
print(s)

#10. Case Study: Sum Dictionary Values
'''
Problem: Calculate the total marks from a dictionary of subject marks.
Test Case:
Input: {'Math': 70, 'English': 80, 'Science': 75}
Output: Total: 225
'''
#solution
print("enter no of subs: ",end="")
n=int(input())
d={}
t=0
for i in range(n):
    e=input()
    m=int(input())
    d[e]=m
    t=t+m
print(d)
print(t)

#11. Case Study: Reverse List
'''
Problem: Reverse a list using a loop.
Test Case:
Input: [10, 20, 30]
Output: [30, 20, 10]
'''
#solution
print("enter the no of elements: ",end="")
n=int(input())
l=[]
r=[]
for i in range(n):
    a=int(input())
    l.append(a)

for i in range(len(l)-1,-1,-1):
    r.append(l[i])
print(l)
print(r)

#12. Case Study: Login Verification
'''
Problem: Use `==` operator to check if entered username matches the stored one.
Test Case:
Input: Stored = admin, Entered = admin
Output: Login Successful
'''
#solution
stored=["jacky","julie","uncle","bhimma"]
print("please enter the admin name: ",end="")
entered=str(input())
for i in range(len(stored)-1):
    if(stored[i]==entered):
         print("login successful")
    else:
        continue

#13. Case Study: Library Book Count
'''
Problem: Loop through a dictionary to find the total number of books.
Test Case:
Input: {'Math': 5, 'History': 4, 'English': 6}
Output: Total Books: 15
'''
#solution 
print("enter no of book varities: ",end="")
n=int(input())
d={}
t=0
for i in range(n):
    e=input()
    m=int(input())
    d[e]=m
    t=t+m
print(d)
print(t)

#14. Case Study: Divisibility Checker
'''
Problem: Print numbers divisible by 3 from 1 to 20 using a loop.
Test Case:
Output: 3, 6, 9, 12, 15, 18
'''
#solution
print("enter the start: ",end="")
s=int(input())
print("enter teh end: ",end="")
e=int(input())
for i in range(s,e+1):
    if(i%3==0):
        print(i ,end=" ")


#15. Case Study: Compare Two Lists
'''
Problem: Use a loop and operator to compare elements of two lists and print common
items.
Test Case:
Input: [1, 2, 3] and [2, 3, 4]
Output: [2, 3]
'''
#solution
l1=[1,2,3]
l2=[2,3,4]
r=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if(l1[i]==l2[j]):
            r.append(l1[i])
print(r)

#16. Case Study: Vowel Counter
'''
Problem: Count the number of vowels in a word using loop and condition.
Test Case:
Input: 'education'
Output: 5
'''
#solution
print("enter the word: ",end="")
w=input()
c=0
for i in range(len(w)):
    if(w[i]=='a' or w[i]=='e' or w[i]=='i' or w[i]=='o' or w[i]=='u'):
        c=c+1
print(c)


#17. Case Study: Duplicate Remover
'''
Problem: Remove duplicates from a list using a set and convert back to list.
Test Case:
Input: [1, 1, 2, 3, 3]
Output: [1, 2, 3]
'''
#solution
l=[1,1,2,3,3]
s=set()
print(l)
for i in range(len(l)-1):
    s.add(l[i])
print(s)
s=list(s)
print(s)


#18. Case Study: Student Rank
'''
Problem: Store and display student names with ranks using dictionary (Rank as key).
Test Case:
Input: {1: 'John', 2: 'Alice'}
Output:
1 - John
2 - Alice
'''
#solution
print("no of students: ",end="")
n=int(input())
d={}
for i in range(n):
    s=input()
    r=int(input())
    d[r]=s
print(d)

for r in d:
    print(f"{r} - {d[r]}")

#19. Case Study: Nested Loop - Coordinate Printer
'''
Problem: Print all coordinate pairs from two ranges using nested loops.
Test Case:
Input: range(2) and range(3)
Output:
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
'''
#solution
print("enter x: ",end="")
x=int(input())
print("enter y: ",end="")
y=int(input())
for i in range(x):
    for j in range(y):
        print(f"({i},{j})")

#20. Case Study: Password Strength
'''
Problem: Check if a password contains both digits and letters using loops and operators.
Test Case:
Input: 'pass123'
Output: Strong Password
'''
#solution
print("enter the password: ",end="")
p=input()
d="f"
a="f"
for i in p:
    if(i.isalpha()):
        a="t"
    if(i.isnumeric()):
        d="t"
if(a=="t" and d=="t"):
    print("its strong password")