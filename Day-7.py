'''
Sequences --> Strings,Lists,Tuples,Sets,Frozensets,Dicts

Strings --> A String is a group of characters,It is immutable,ordered,Indexed,Collection.We can denote it in single,double or triple quotes..

data = '' #empty string
print(type(data))
print(len(data))

#operations --> Concatenation,Repetition,Indexed,Slicing
#Concatition --> combinig multiple strings
sub1 = "Python"
sub2 = "MYSQL"
print(sub1+sub2)
#output should be python,mysql
#python <-> mysql
print(f'{sub1},{sub2}')
print(sub1+" <-> "+sub2)

#Repetition --> String can be repeated any number of items with  a valid int 

print("*")
print('*' *10)
name = "Mamatha";place = "vizag"
print(f'{name * 10}*')
print(f'--->{name} is in --->{place}')

#Membership --> in,not in
print("tha" in "mamatha")
print("THA" in "mamatha") #returns False

name = 'python'
print(name)
print(len(name))
#Traversing the elemnts --> Positive Indexing
print(name[2])
print(name[4])
#print(name[8])
#Negative Indexing --> starts from back it is denoted as -1 to len(obj)
print(name[-1])
print(name[-4])
print(name[-0])
#print(name[-9]) #IndexError
'''
#Slicing --> group of characters --> [start:end] start is included,end is excluded (len(obj) -1)
name = 'mamathasri'
print(name[:]) #returns all characters
print(name[0:7])
print(name[ :4])
print(name[2: ])
print(name[4:24]) #returns till end of string
print(name[24:]) #returns empty
print(name[6:1]) #returns empty string as positive slicing lower index to higher index

#name[2] = "saketh" #strings are immutable

name = "codegnan"
print(name)
print(name[-1:])    #returns only last character
print(name[-5:-1])  #same including negative indices with same symbols lower to higher index
print(name[-8: ])
print(name[-9:-1])
print(name[-6:-4])
print(name[:-6]+name[-6:])
print(name[-1:-4])  #returns empty string
print(name[0:11])
print(name[1:-1])
print(name[-1:3]) #returns empty

#Striding --> [start:end:step]
name = "codegnan"
#print(name[::0]) #returns ValueError
print(name[::1]) #returns complete string
print(name[::2]) #skips each alternate element from beginning
print(name[::3])
print(name[6::])
print(name[::8])
print(name[6::11])
print(name[-6::-2])
print(name[4::-4])
print(name[8::8])
print(name[-6::18])
print(name[28::1])
print(name[4::8])
print(name[9::7])

place = "Visakhapatnam"
print(place[:4])
print(place[7:])
print(place[-6:])
print(place[1:7:2])
print(place[-8:-6-3])
print(place[-1:-4:-7])
print(place[:8])
#what if we give -1 in interval
print(place[::-1]) #this helps in return in reverse order
print(place[::-2]) #this skips one element in reverse order
print(place[1:5:9])
print(place[1:9:2])
print(place[-9:-1:1])
print(place[-0:-5:-8])
print(place[4:23:9])
print(place[::3])

#Built-in functions --> type(),len(),min(),max(),ord(),char(),sorted()

password = "admin123"
print(len(password))
print(type(password))
print(min(password))  #min() returns min object in collection
#ASCII values follows
print(ord('A'))
print(ord('a'))
print(ord('z'))
print(chr(120))
print(sorted(password))
