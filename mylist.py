mylist=['nitish', 'name', 'satyam', 'sun v', 'gaurav', 'vikash', 'nilesh', 'harshit', 'vishal', 'rohan']
'''for x in range(10):
    a=input()
    mylist.append(a)'''
print(mylist)
print("updating the mylist by using update\n")
mylist[1]="names"
print(mylist)
list1=[1,23,456]
print("inserting list1 in mylist\n")
mylist.extend(list1)
print(mylist)
print("updating the new mylist\n")
mylist.insert(3,"papa")
mylist.insert(4,'mummy')
mylist.insert(5,'dada')
print(mylist)
a=len(mylist)
print("the length of length\n",a)
print("remove the word by delete\n")
del mylist[5]
print(mylist)
print("remove the word by remove method\n")
mylist.remove(456)
print(mylist)
print(type(mylist))
print("Done..............")
