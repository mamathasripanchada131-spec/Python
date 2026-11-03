'''#Q1)
n = int(input("Enter the sales"))
if n>1000:
     print("Best Seller")
else:
    print("No Output")

#Q2)
raining = bool(input())
print(raining)
print(type(raining))
if raining:
    print("Extra Rain Charges Applied")
else:
    print("No Output") #We will get this when we dont pass any input

#Q3)
order_value = int(input("Enter the Order Value:"))
if order_value > 99:
    print(f'Final Bill Amount:{order_value}')
else:
    print(f'Final Bill Amount:{order_value}+30')

#Q4)
Budget = int(input("Enter the Budget:"))
if Budget>10000:
    print(" Plan: Trip:")
elif Budget>5000:
    print("Plan: Resort Stay:")
elif Budget>3000:
    print("Plan: Movie and Dinner:")
elif Budget>1000:
    print("Plan: Cafe and Shopping:")
elif Budget>500:
    print("Plan: Street and park visit:")
else:
    print("Plan: Stay Home:")


#Repetition Statements (Loops) --> Loops helps us in automating repetitive tasks --> for, while
#Usage of for: --> It is used mainly to iterate within in lists, strings, ranges..

Syntax :
for <temp> in collection/range:
      statement(s)...
      .....
      .....

marks = [25,20,21,19,10,12]
#Marks can be dynamic
marks = list(map(int,input("Enter the marks:").split(',')))
for i in marks:
    print(i) #it traverses within the loop
#Calculate the total marks

marks = list(map(int,input("Enter the marks:").split(',')))
total = 0
for mark in marks:
    #print(i) #it traverses within the loop
    #We need to update total with each mark
    total = mark + total  #total += mark
    print(total)
print(f'Total marks are:{total}')
print(f'Avg marks are:{total/len(marks)}')

subject = input("Enter the subject:")
for i in subject:
    print(i)
    
details = {'ids':[121,123,125],
           'marks':[25,20,21]}
for data in details: #indexed through keys
    print(data)
    print(details[data]) #it returns values

for data in details.values():
    print(data)
for key,value in details.items():
    print(key,value)

#range(stop) --> takes by default minimum value ass 0
for i in range(5):
    print(f'Value of i is{1}')
    print(f'Square of i is {i**2}')

#range(start,stop) --> u can mention start and stop postns(values)
#start is included,end is excluded
for i in range(1,11):
    print(i,i**2)
    print('<----->')

#range(start,stop,step)
for i in range(1,21,1):
     print(i)
for i in range(1,21,2):
    print(i)

#Get first 10 even numbers
#print numbers from 10 to 1 in reverse order

for i in range(10,0,-1):
    print(i)

#print 'A' to 'Z' in a single line

for i in range(65,91):
     #print(i,chr(i))
     print(chr(i),end='')

#ord-->('s') and chr('i')

names = ['Mamatha','Pavithra','Swathi','Devi','Parvathi']
for name in names:
    print(name,end=' ') #this returns in horizontal order

for i in range(len(names)):
    print(names[i]) #names[0] --> Mamatha -->names[1] --->Pavithra

#Ask integer input from user and get the sum of numbers as per input

Test-1:
4
10

Test-2:
6
21

Test-3:
-5
No Output

n = int(input("Enter a Value"))
if n>=0:
    result = 0 #target
    for i in range(n+1):
      #print(i)
      result = result + i
    print(f'Result of {i} is {result}')
else:
    print("No Output")
'''

#Usecase: Checking daily workout app usage
work_log = [1,1,1,0,1,1,0]
#1 -->workout done
#0 -->workout missing
#Find the longest workout streak
longest_streak = 0#target
current_streak = 0
for day in work_log:
    #print(day)
    if day == 1:
        current_streak = current_streak + 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0
print(f'longest streak is {longest_streak}')


