'''
Operators --> operators help us to perform operations between operands
Arithmetic Operators -->+,-,*,/,**,//(Integer or Floor Division),%(Modulus --> remainders)

Assignment Operators --> It helps to assign,update(increment),decrement values

# = (assigning), += (Addition&Assign), -=(Subtraction&Assign),
# *=(Mulitiplication&Assign) /=,//=,**,%=
'''
'''data = 20
print(data)
print(type(data))

stock = data
print(stock)

#Increment the value of stock
stock = stock + 5 #stock+=5
print(stock)
print(data)

#decrement the value of the data by 2 values
data=data-2
print(data)

data*=2
print(data)
stock-=data #stock = stock - data
print(stock)

stock = 100
stock** = 2
print(stock)


#Comparision Operators (Relational Operators) -->It performs comparision
#between the operands and results in boolean True/False --> Conditions
# ==,!=,<,<=
,>,>=
namae = 'mamatha'
mamatha_attendence = 75

print(mamatha_attendence >= 75)
print(mamatha_attendence == 80)
print(mamatha_attendence >= 80)
print(mamatha_attendence <= 80)
print(mamatha_attendence < 80)
print(mamatha_attendence > 80)
print(mamatha_attendence != 80)

#Logical Operators --> and,or,not (keywords)
#and --> it needs all conditions to be satisfied (two or more)
#or --> it needs any one condition to be satisified
#not -->opp to existing

max_marks = 80
mamatha_marks = 75
max_att = 7
5
mamatha_att = 70

mamatha_marks +=10
certificate = mamatha_marks >= max_marks and mamatha_att >= max_att
print(certificate)
chance = mamatha_marks >= max_marks or mamatha_att >= max_att
print(chance)
data = []
print(data)
print(not(data)) #returns True
data = [1,2,3,4]
print(not(data)) #returns Flase as data is existing
#Both Logical and Comparision operators will return result in Boolean

#Membership Operators --> IN, NOT IN
#check for the existance in a sequence(str,list,set,tuple,dict)
names = ['mamatha','mani','kalyani','kalyan']

name = 'mahi'
print(name in names) # returns False
print(name not in names) #returns True
print('12' in '121')
#print(12 in 121) #TypeError as we have taken int type

print('ajay' in 'ajay kumar')
print(['ajay'] in ['ajay']) #returns False as its a list

#Identity Operators --> It specifically refers to the object (memory location)
#id -->is,is not

a = 15
b= 15
print(a==b)
print(id(a))
print(id(b))
c = a
print(id(c))

print(c is a) #as id of both a and c are same --> True

a = [1,2,3,4]
b = [1,2,3,4]
print(a == b)
print(id(a))
print(id(b))
#as we have taken two lists eventhough with similar values identity
print(a is b)

c =  a
print(id(c))
print(c is a) #returns True as we are assigning same object

a = (1,2,3)
b = (1,2,3)
print(id(a),id(b))
print(a is b)

#When we check with the Interpreter mode and scripting mode above
#tuple result changes

#Logical,Membership,Identity,Comparision(relational) -->always result is in boolean

#Bitwise Operators -->It performs Bitwise operators --> &(Bitwise and)
#|(Bitwise OR),^ (Bitwise XOR)
#An integer will be converted binary format and performs bitwise operation
#following integer to binary conversation

print(7&3)
print(7|3)
print(7^3) #XOR operation it returns 4
#7 to binary --> 0111
#3 to binary --> 0011
#7^3 --> 0100

#Shifting Operations (<<,>>)

print(7 << 1)
print(7 >> 1)
