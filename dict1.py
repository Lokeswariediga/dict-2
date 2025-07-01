# 1.Create a dictionary from two lists:
# 	keys = ['id', 'name', 'age']
# 	values = [101, 'John', 25]

keys = ['id', 'name', 'age']
values = [101, 'John', 25]
res=dict(zip(keys,values))
print(res)
output:
{'id': 101, 'name': 'John', 'age': 25}

# 2.Create a dictionary to store student name and age.
res=[{"Name":"priyanka","Age":"25"},{"Name":"ammu","Age":"23"}]
print(res)
output:
[{'Name': 'priyanka', 'Age': '25'}, {'Name': 'ammu', 'Age': '23'}]

# 3.Create an empty dictionary and add key-value pairs one by one.
res=dict()
spc["name"]=input("enter name:")
spc["pin"]=input("enter pin:")
spc["city"]=input("enter city:")
res.append(spc)
print(res)
   output:
enter name:priyanka
enter pin :500073
enter city: bangalore

# 4.Get the value of key "salary" from this dictionary:
#                     EX: employee = {'name': 'John', 'age': 30, 'salary': 50000}

employee = {'name': 'ammu', 'age': 25, 'salary': 50000}
print(employee['salary'])
output:
50000

# 5.	 Remove the last inserted key-value pair from the dictionary using an appropriate method
res={'name': 'ammu', 'address': 'bangalore', 'pin': '700153',"rollno":"154"}
res.popitem()
print(res)
output:
{'name': 'ammu', 'address': 'bangalore', 'pin': '700153'}

# 7.Define packing and unpacking in Python. Also, provide one example for both packing and unpacking

Packing:
    packing refers to the process of putting multipe values into a single varable(usually a tuple or list).
Example:
data=("ammu",25,"hyb")
print(data)
Output:
ammu, 25,hyb

Unpacking:
      Unpacking means extracting those individual values back from that packed variable.
Example:
data=("ammu",25,"hyb")
data= name,age,city
print(name)
print(age)
print(city)
Output:
ammu
25
hyb



