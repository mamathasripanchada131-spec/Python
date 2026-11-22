'''#Basic Exception handling
a,b=5,0
try:
    result=a/b
    print(f'Answer is {result}')
except: Exception as e:
    print(f'Error is {e}')

#a,b = map(int,input("Enter the Values:").split())
#print(a,b)
try:
    a,b = map(int,input("Enter the values:").split())
    print(a,b)
    result = a/b
    print(f'Answer is {result}')
except Exception as e:
    print(f'Error is {e}')

#Multiple Exception Blocks
try:
    a,b = map(int,input("Enter the values:").split())
    #print(a,b)
    result = a/b
    print(f'Answer is {result}')
except ValueError:
    print("Values should be only 2 and only integers")
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("Sariga chusi rayuuu")
  
try:
    subjects=['Python',45,'AI',30]
    #print(subjects[5])
    subjects.append("SQL")
    print(subjects)
except Exception as e:  #this can be written if u want exception to take carr
    print(e)
except IndexError:
    print("make sure to check the length")
except NameError:
    print("Check the spelling")
except AttributeError:
    print("check the method properly")
finally:
    print("Anyways this will be printed...")

#Catching Multiple Exceptions Together
try:
    value = int(input("Enter a value:"))
    #result = 10/vale #vale check this case
    f = 10/value
    print(f)
except (ValueError,ZeroDivisionError,NameError) as e:
    print(f'An Error occured:{e}')

'''#Raising Exceptions
#you can raise exceptions intentionally using raise keyword
'''value = 15
if value <0:
    raise ValueError("Value cannot be negative")
else:
    print("Done")

Custom Error Messages:
try:
   raise Exception("Custom Error Message")
except  Exception as e:
    print(e)

try:
    value = -15
    if value < 0 or value in [1,20]:
        raise Exception("Value cannot be negative")
except Exception as e:
    print(e)


#File Handling --> open()

#File and Directory operations are essential to store the data..
#python provides build-in function --> open()
'''
#mode of operations --> 'r','w','r+','w+'
#open(filename,mode) #default mode is 'r'
try:
    d = open('new.txt','r')
    print(d)
    print(d.read()) #reads the entire content
    print(d.readline())  #reads a single line
    print(d.readlines())  #read all lines into a list
except Exception as e:
    print(e)












