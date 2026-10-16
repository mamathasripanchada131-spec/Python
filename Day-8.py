'''
String Methods --> Case converstions,Replacing,Finding,White Trailing spaces,testing methods,alignment methods

#Case Converstions --> upper(),lower(),title(),capitalize(),swapcase()
data = "codegnan"
print(type(data))
print(dir(data)) #dir() returns the available methods/functions
#upper() --> converts object to uppercase
print(data.upper())
e = data.upper()
print(e)
#lower() --> converts objects to lowercase
f = data.lower()
print(f)
#capitalize() --> it will capatialize the first letter in the word
print("codegnan vizag".capitalize())
#title() --> it will capitalize every first letter in each word
print("codegnan vizag".title())

print("coDEgnan".swapcase()) #converts uppercase to lower and lower to uppercase.

#Testing methods (which will give the results as Boolean (True/False)
#isupper(),islower(),isalnum(),isdigit()...

print("Codegnan".isupper())
print("codegnan".islower())
print("123987".isupper())
print("3560875".islower())
print("ATYUuyt".islower())
print("admin1223".isalpha()) #returns True only when we have all alphabets
print("admin".isalnum()) #returns True for an alphanumeric string
print("6547579".isdigit()) #it checks for a digit string
print("Python".istitle()) #returns True
print("Python aptitude".istitle()) #returns False
print("Python".startswith('P'))

data = "Python Aptitude"
print(data.startswith("A"))
print(data[7:].startswith("A"))
print(data.startswith("A",7))
print(data.isupper())
print(data.endswith("e"))
print(data.endswith("n",0,6))
print(data.endswith("o",0,5))

print("12.34".isalnum())
print("12.34".isdigit())
print("1/2".isnumeric()) #fractions,roman numericals
print("xii".isnumeric()) #roman numericals but we need to encode the data and get it

#Finding and Searching methods -->find(),index(),count()

data = "Codegnan is in Vizag"
print(data.find('a')) #returns only the first occurance
print(data.find('a',7)) #here we will check for the next occurance
#find() will return -1 if the giiven object is not present
print(data.rfind("a")) #rfind() will return the last occurance
#index(),rindex()
print(data.index("a")) #returns the first occurance
#if given object is not present it raises ValueError
#print("qwerty".index("s")) #raises ValueError
print("qwerty".index("werty")) #as substring is starting with 'w'
#rindex() returns last occurance
print("qwertywerty".rindex("y"))
#count() will return total number of occurance
print("Codegnan".count("t")) #return 0 as 't' is not present
print("Codegnan".count("n"))

#split(),join(),strip(),lstrip(),rstrip(),zfill()
#split() returns the list of substrings from the string using separator
a = "Python Aptitude Softskills MYSQL"
b = a.split() #by default space is treated
print(b)
a = "Python,Aptitude,Softskills.MYSQL"
c = a.split(',')
print(c)
#join()
print("code".join("gnan")) #concatenates every object with the given iterable
print("#".join("Codegnan"))
print(" ".join("mamatha"))
print("&".join("sri"))

#While Space & Trimming methods --> strip(),lstrip(),rstrip()
a = "Saketh"
print(len(a))
a = a.strip() #removes leading and trailing Whitespaces
print(len(a))
a = a.rstrip()

#Alignment Methods -->zfill() (make sure to pass the width>len(obj) it pads zero from left)
print("python".zfill(10))
print("Codegnan".zfill(1))
print("python".center(10,'*'))
print("mamatha".isupper())
print("python".ljust(10,"*")) #returns the leftjustified string with fillchars
print("python".rjust(10,"*")) #returns the rightjustified string with fillchars
'''
#Sequences --> Lists[],Tuples(),Sets set(), Frozensets,Dicts {}
