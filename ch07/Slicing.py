list1 = range(5)  
print(list1)
print(list(list1))
print (list1[2:4])          # python 2
print (list(list1[2:4]))    # python 3
print (list1[2:])
print (list(list1[2:]))
print (list1[:2])
print (list(list1[:2]))
print (list1[:])
print (list(list1[:]))
print (list1[:-1])
print (list(list1[:-1]))
list1=[0,1,2,3,4]
try:
  list1[2:4] = [8, 9] # python 3.x
except:
  list1[2] = 8  # python 2.x
  list1[3] = 9

print(list(list1))
print(list1)


