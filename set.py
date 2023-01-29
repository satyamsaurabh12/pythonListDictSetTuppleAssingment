myset={"mobile","teachnook","satyam saurabh","mobile"}
print(myset)
print("adding the some data")
myset.add("january")
print(myset)
set1={1,23,4,5,67,8}
set2={2,456,789}
print("mersing the data in set3 of set1,myset\n")
set3=set1.union(myset)
print(set3)
print("deleting the item in set3\n")
set3.remove("mobile")
print(set3)
myset=myset.intersection(set3)
print(myset)




