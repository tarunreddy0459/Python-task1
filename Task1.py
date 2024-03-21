list1 = ["apple", "orange" , "dragonfruit"]

dict1 = {'name': 'Vamshi', 'age': 20, 'city': 'Hyderabad'}

set1 = {1, 2, 3, 4, 5}

list1.append("grapes")
dict1['gender'] = 'Male'
set1.add(6)

list1.remove("orange")
dict1.pop('age')
set1.discard(3)

list1[0] = 'kiwi'
dict1['city'] = 'Delhi'
set2={6,7,8}
set1.update(set2)

print("list:", list1)
print("dictionary:", dict1)
print("set:",set1)