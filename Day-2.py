'''name="mamathasri"
age=22
place="narshipatnam"
#print(names)#it raises NameError
#print(Age)
#Python is case-Sensitive
email_id = "mamathasri@codegnan.com" #snakecase Convention(multiple words)
print(email_id)
branch_1="vijayawada" #we can use number anywhere but not at the start
print(branch_1)
#comments --> It wil make uers understand what it conveying
#Single line comment --> #
#Multi Line Comments --> WE can use triple quotes (Doc String)

#Multiassignment of variables #makes sure to pass same number of values
name,email_id,mobile,gender="mamathasri","mamathasri@codegnan","9573322131","female"
print(name,mobile)
#Python by default follows Implicit type(user need not allow)

#So u can prefer single line or multiple lines for assigining variables

name= "codegnan"; age=8;place="vizag"
print(name,age)

#Deletion --> del
del age #permanent deletion
del name,place
print(age)
'''
'''#Swapping of variables
a,b = 15,25
print(a)
print(b)
a,b=b,a #value of a will become b
print(a)
print(b)

c = a #reassigning the existing value to a new variable
print(c)
'''
"""
#Literals --> These are constants such as numbers(int,float,complex)
#"hello" "good"
age = 32
print(age)
taste = "bad"
print(taste)
price = 115.54
print(price)
print(type(price)) #it returns the type of object
#type() is very very imp
print(type(age))
"""
'''
#Identifiers --> names given to variables,functions,classes,objects,modules

#Punctuators --> [] --> Lists,() -->Tuples,{} --> Dictionaries,Sets
#Operators --> There are different type of operators --> operations
#+,-,*,**,/ (Arithmetic operations),//,%
a = 5
b = 3
print(a/b) #/ --> Float Division (answer is always in float value)
print(a//b) #Flooring Division (Integer division) returns quotient
print(a%b) #Moduls --> returns remainder
'''
#Raju purchased Shoes with price 1000,discount 15%,
#now how much Raju has to pay?

price = 1000
discount = 0.15
final_price = price -(price*discount)
print(final_price)

#Vijay went to hotel for dinner his bill is 2500,GST applicable is 5%
#hotel manager has given him 5% discount. how much he has to pay?

price = 2500
gst = 0.05
discount = 0.05
#first apply discount
final_price = price -(price*discount)
#print(final_price)
final_price = final_price + (final_price*gst)
print(final_price)
