'''
Datatypes -->Numeric datapes --> int,float,complex
-->Boolean datatype -->True/Flase
None type
-->Sequences -->str,lists[],tuples(),sets set(),mappings (dictionaries)
{},frozenset
'''
'''#Lists --> A list is an Ordered,Mutable,indexed and Heterogrnous Collection
#We use [] to reprsent lists
#Students details,Order datails, Stock entires...
details = [1,'mamatha','PFS','narshipatnam',36.3]
print(len(details))
print(type(details))

stu_ids = ['CGVI0134','CGVI0135','CGVI0136']
#print(stu_ids[1])
stu_ids[0] = 'codegnan' #here we are using indexing
print(stu_ids)

#Tuples --> Tuples are also Immutable,Ordered,Indexed and heterogenous
#collections, we use () parenthesis
#dimensions,coordinates
places =('tirupathi','vijayawada','vizag')
print(places)
#print(len(places))
#print(type(places))
places[0] = 'chennai' #it is not possible as tuples 
print(places)

dimensions = 10,20,30  #by default it becomes tuple
print(dimensions)
print(type(dimensions))

#Sets --> A Set is a Unique collection (removes duplicates)
#A set is an Unordered,Unindexed,Mutable collection)
ids = set() #empty set
print(ids)
ids = set([123,134,135,123])
print(ids)
ids = set() 
print(ids)
ids = set((123,134,135,123))
courses = {'PFS','JFS','DA'}
print(courses)
print(type(courses))
print(courses[0]) #As Set is unordered there is no index

#Dictionaries --> A dictionary (mapping object) is a collection of
#Key value pairs --> dict = {k:v}
#Dictionary is also mutable collection
#Keys must be unique in a dictionary (Keys can be int,float,str)
details = {'branch':'Vizag',
           'batches':['PFS-VSP-007','PFS-VSP-006','PFS-VSP-005',
                      'PFS-VSP-004'],
           'course':'PFS',
           'count':'19'}
print(details)
print(type(details))
print(len(details))
print(details['batches']) #we access by giving only keys

#Every built-in datatype is a built-in function
#int,float,complex,bool,str,list,tuple,set,dict
#Lists --> tuples,sets,dict,str
marks = [35,24,54]
a = tuple(marks)
print(a)
b = set(marks)
print(b)
#c = str(marks) #it makes every symbol as a charcter
#print(c)
#print(len(c))

marks = [35,24,54]
#d = dict(marks) #its not possible like this
e = dict.fromkeys(marks) #we need to use fromkeys()
#taken will become keys and values will be None
print(e)

#Tuple --> list,set,str,dict
#Sets --> list,tuple,str,dict

#Dictionaries --> lists,tuples,sets
ids = {1:123,2:124}
a = list(ids) #it will only fetch keys
print(a)
b = tuple(ids) #it will only fetch keys
print(b)
c = set(ids) #it will only fetch keys
print(c)
d = str(ids) #every symbol/object will be a character
print(d)
print(len(d))
#Frozensets -->It is an imutable set,Unindexed,Unordered
a = frozenset((12,32,12,32))
print(a)
print(type(a))
print(len(a))
b = list(a)
print(b)
c= tuple(a)
d = set(a)
e = dict.fromkeys (a)
f = str(a)
print(c,d,e,f)
print(len(f))

d = 'mamatha'
e = list(d)
f = tuple(d)
g = set(d)
h = dict.fromkeys(d)
print(e,f,g,h)
'''

#Operators --> Arithmetic operators,Assignment,Comparision,
#Logical,Membership,Identity,Bitwise operators

#Arithmetic --> +,-,*,/(float division),//(floor division) Quotient
#% Modulus(remainder),**(Exponential)
a = 3
b = 2
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)



