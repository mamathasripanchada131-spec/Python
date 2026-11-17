'''
Built-in Functions --> Funtions which are inbuilt python abs(),any(),all(),bin(),bool().....

dir(__builtins__) -->enumerate(),zip()
'''
details = ['Codegnan','Mamatha','PFS-VSP-007']
'''
0 : Codegnan
1 : Mamatha
2 : PFS-VSP-007

for i in details:
    print(details.index(i),':',i)

for i in range(len(details)):
    print(i,':',details[i])

for i,j in enumerate(details):
    print(f'{i} : {j}')

#enumerate() will create a counter object for an iterable
#zip() will combine multiple iterables into a single iterable

data = ['Malika','Maha','Mamatha']
marks = (20,25,24)
#place = ('vizag','vjwda','hyd')
details = dict(zip(data,marks)) #if we take one more iterable it raises ValueError
print(details)

emails = input().split()
print(emails)
for email in emails:
    print(email.split('@')[1])

orders = list(map(int,input().split()))
print(orders)

#eval() --> You can take any input --> dict
salaries = eval(input("Enter the Salaries:"))
print(salaries)
print(type(salaries))

print(int(4.56))
print(round(4.56))  #round() it will round off to next decimals/nearest values
print(round(4.567,2))
'''
#Function is termed as First class Object
#Recursive Functions --> A Function calling itself,where it makes the smaller problem is broken into multiple times...
#depends on two cases --> Base case (it indicates when to stop recursion)
                  #--->Recursive case(it makes the problem to be repeated
#Suitable for Tree Structures,Graph Traversal...

'''
Syntax:
def function():
     if base_condition:
         return
     function()   #we write our recursive
function()

#Factioral Approach using Recursion

def factorial(n):
    """Recursive Approach"""
    if n==0 or n==1:
        return 1
    elif n <0:
        return "No -ve values only +ve values to be accepted"
    else:
        return n*factorial(n-1)
n = int(input("Enter a value:"))
print(factorial(n))
'''
#Sum of natural numbers using recursive logic
#5 --> 15 #1+2+3+4+5

def sum(n):
    """Recursive Approach"""
    if n==0 or n==1:
        return 1
    elif n <0:
        return "No -ve values only +ve values to be accepted"
    else:
        return (n+(sum(n-1)))
n = int(input("Enter a value:"))
print(sum(n))

'''
Task:Build a simple choice chooser:
1 --> Recursion logic Factioral
2 --> Sum of Natural numbers (recursion)
3 --> BMI Calculation
4 --> Fibonacci Series
5 --> ATM Usecase
any other number --> only enter 1-5
Q --> Quit
'''


































