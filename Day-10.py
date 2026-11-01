d ={12,3,4,(12,3,4),45}
print(d)
print(len(d))
print(len(d)) 

#Task: Create a Nested tuple with list inside it and make it call methods of list in tuple

a = ([1, 2, 3], (1, 2, 3), 3, 4, [6, 7, 8])

#print(a)
#print(type(a))
#print(len(a))
# ([1, 2, 3], (1, 2, 3), 3, 4, [6, 7, 8])
#<class 'tuple'>
#5

# Indexing
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[0][1])
print(a[1][2])

# Slicing
print(a[0:3])
print(a[1:4])
print(a[:3])
print(a[2:])
print(a[:])

# Striding
print(a[::2])
print(a[1::2])
print(a[::-1])
print(a[::3])

print(a[0])
print(a[0][0])
print(a[0][1])
print(a[0][2])

print(a[4])
print(a[4][0])
print(a[4][1])
print(a[4][2])
a[0].extend([5, 6])
print(a)

print(a + (5, 6))

print(a * 2)

print(a.count(3))
print(a.count(4))
print(a.count([1, 2, 3]))
print(a.count((1, 2, 3)))

# index()
print(a.index(3))
print(a.index(4))
print(a.index([1, 2, 3]))
print(a.index((1, 2, 3)))
