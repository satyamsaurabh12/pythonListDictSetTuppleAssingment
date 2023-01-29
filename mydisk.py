mydisk={
"name":"satyam saurabh",
"work":"on disctionary",
"college":"IIITDM KURNOOL",
"place":"A.P",
}
print(mydisk)
print("updating data\n")
mydisk["name"]="shashank"
print(mydisk)
mydisk["place"]="KURNOOL , A.P"
print(mydisk)
print("introducing the data\n")

mydisk['course']="c++,c,java,javascript"
print(mydisk)
print("deleting the data\n")
mydisk.pop("course")
print(mydisk)
print("enter the data type",type(mydisk))
a=len(mydisk)
print("\n the length of this data type\n",a)



