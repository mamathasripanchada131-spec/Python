'''#input formating --->input()
#usage of input()
# we can pass any type of object as input -->result in string

name = input("1234")
print(name)
print(type(name))

# integer input --->int() --> if you  missmatch value -->value error
roll_number = int(input("enter the roll number:"))
print(roll_number)
print(type(roll_number))

# float input -->float()-->we can pass either / decimal value-->float
marks = float(input("enter the marks:"))
print(marks)
print(type(marks))


# Group of strings (multiple values as Strings)
# space separated values -->we need to give one space after each object
#returns list
# names =input().split() -->no need in computative exms
names = input("enter the names:").split()
print(names)
print(type(names))

#comma separated values

subjects = input("enter the names:").split(',')
print(subjects)
print(type(subjects))


#multiple values (more than one)strings
#make sure to match the argument
name,batch =input("enter the name:").split()
print(name)
print(batch)

#multi integer values

order_id,cost = map(int,input().split())
print(order_id)
print(cost)

# we want to take subjects marks
p_marks,ap_marks,ss_marks,sql_marks = map(float,input().split())
print(p_marks,ap_marks,ss_marks,sql_marks)


#group of Integer ,float values
stu_marks = list(map(int,input("enter the marks:").split(',')))
print(stu_marks)

discounts = list(map(float,input("enter the discounts:").split(',')))
print(discounts)

#accepts the cost of selling the product from user and also the original cost
#of the product and determine the profit /loss amount of the user

original_amount = float(input("enter the original cost:"))
selling_amount = float("enter the selling_cost:")
profit = selling_amount - original_amount
print(profit)


# set of integers
# set of floats values -->replace int with float
ids = set(map(int,input("enter the IDS:").split(' ,')))
print(ids)
print(type(ids))

#passing list() as input using eval()
list_data = eval(input("enter the values:"))
print(list_data)
print(len(list_data))
tuple_data = eval(input("enter the values:"))
print(tuple_data)
print(len(tuple_data))
set_data = eval(input("enter the values:"))
print(set_data)
print(len(set_data))

#passing dict data using eval
stu_details = eval(input("enter the values:"))
print(stu_details)

# so using eval() u can pass any type of data
#output formatting ---> print()
a,b,c = map(str,input("enter the names:").split())
print(a,b,c)
# now we will use sep
print(a,b,c,sep="----")
#end is specially telling how u wanna end the statements 
print(a,b,c,sep=":",end="\t") #here end = tab space character 
print("gowthu","vizag",end=" ") #here end = space character
print(45,3.4)

# 1) using commas in print()
name = "codegnan";branch ="vizag";batch ='PFS-VSP-007'
print(name,"is in",branch)
print(batch,"belongs to", branch ,"branch")

# 2) using %(modulus) formatting --->old style c programming
# %d --->integers ,%f-->float,%s-->strings
age = 22
price =45.231
place ="vizag"
print("age = %d| price = %f | place = %s"%(age,price,place))
print("price is %.f"%price)# in this case complete decimal part is wiped
print("price is %.2f"%price)# rounding off to two decimals
