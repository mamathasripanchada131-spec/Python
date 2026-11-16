'''#Pass by Reference -->When mutable objects (Lists,Sets,dict) are passed introduction
#the function,changes inside the function affect the original object...

def update(items):
    """We will assume item as list"""
    #items.append("Laptop")
    items.extend(["Laptop","Power Bank","Camera"])
cart = ["Mobile","Watch"]
print(update(cart)) #returns None
print(cart) #original list changes
#print(update("mamatha")) #raises Attribute Error

#Dictonary Usage: --> Updating profile
def update(profile):
    """Usage of Dictionary"""
    profile['branch'] = "Vizag"
students = {'names':['Sanjay','Akash']}
pfs_students = {'batches':['PFS-VSP-007','PFS-VSP-006'],
                'subjects':['Python','MYSQL','Aptitude']}
update(students)
print(students)
update(pfs_students)
print(pfs_students)


#Pass by value -->Original data will not change,Immutable objects
#Pass by Object Reference -->Original data will change,Mutable objects

#Built-in functions -->Functions which are inbuilt in python
#print(),len(),min(),max(),sorted(),int(),float(),bool(),complex()
#str(),list(),tuple(),set(),dict(),input(),eval(),help()

#print(dir())
#print(dir(__builtins__))  #returns list of builtin functions and errors
#print(help(print))
#print(help(len))

#abs(),chr(),ord()
print(abs(-34)) #returns the absolute value of a numbers
print(chr(67))
print(ord('@')) #returns the ASCII value
data = [24,56,21,0]
print(any(data))  #any() --> compares bool(x) for any valuer -->True
print(all(data))  #all() --> needs all values to be present
#print(all(none))
print(all([None]))
print(bin(6))  #returns binary object

print(help(enumerate))

data=["Mamatha","Devi","Swathi"]
c = dict(enumerate(data))  #by default it creates a counter object
print(c)

d=dict(enumerate(data,1))
print(d)
'''
#Zip --> it combines multiple collections into a single collection
data= ["Mamatha","Devi","Swathi","Parvathi","Pavithra"]
marks = [25,20,23,21,18]
f = dict(zip(data,marks))  #zip checks for length matching
print(f)
