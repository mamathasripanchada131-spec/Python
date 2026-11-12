'''# 4. variable length arguments ---> we can capture any number of positional
# arguments ,we use (*args),captures excess positional argumets and
# pack them into tuple..

def sample(*a):
    """ usage of arbitrary arguments"""
    print(a)
    print(type(a))
sample()
sample(1,2,)
sample('gowthami','codegan')
sample([12,14,5,7,9])


#In above case we used '*' to pack the values into a tuple
a,b,c = 2,4,-6
print(a,b,c)
a,*b,c=2,4,5,6,65,12,-12
print(a)
print(b) #in this case all values are stored into list
print(c)
#a,*b,c=2,4,5,6,65,12,-12 #multiple expressions are not allowed..
#print(a)
#print(b)
#print(c)

a,*b,c=2,4,5,6,(65,12,-12)
print(a)
print(b)
print(c)

#Find the sum of values

def add(*a):
        """Usage of variable length arguments"""
        #print(a)
        #print(type(a))
        result = 0
        for value in a:
            #if type(value) in (int,float): #Membership operator
            if type(value) == int or type(value) == float: #Comparision and Logic operator
               result  = result + value
               #print(result)
        return result
#print(add())
#print(add(1,3,4,5)) #1+3+4+5 --> 13
#print(add(12,3,4,5,6,-98,12))
#print(add(1,2,4.6,-2,'codegnan',2,12,'saketh'))
#What if we accept group of values
d = list(map(int,input().split()))
print(d)
print(add(*d)) #We need to use * to unpack the values from the tuple

#We will use above usasge of variable length arguments for ordering pizza

def order_pizza(size,*toppings):
    """Usage of *args"""
    print(f'Size of pizza is {size}')
    print(f"Toppings:{toppings}")
    for topping in toppings:
        print(f'Topping added : {topping}')
order_pizza("Large","Onions","Paneer","Capsicum","Olives","Mushrooms")
'''
#Keyword Variable length arguments:Any number of keyword arguments,
#Data is stored in dictionary,we use **kwargs...

def sample(**a):
    """Usage of **kwargs"""
    print(a)
    print(type(a))
sample()
sample(name="Vinay",batch="PFS-VSP-007",place="Vizag",branch="CSE",course="PFS")


def order_pizza(size,*toppings,**details):
    """Usage of *args"""
    print(f'Size of pizza is {size}')
    #print(f"Toppings:{toppings}")
    for topping in toppings:
        print(f'Topping added : {topping}')
    for key,value in details.items():
        print(f'Data is {key},result is {value}')
order_pizza("Large","Onions","Paneer","Capsicum","Olives","Mushrooms",
            name="Vinay",
            bill=200,
            delivery=False,
            tip=50)


