name = "Tom"
age = 30
hight = 1.80
is_student = False
lst = [15, 2, 30, 44, 5]
dct = {"name": "Tom", "age": 30, "hight": 1.80, "is_student": False}
tpl = (15, 2, 30, 44, 5)
none_value = None

print(age in lst)
print("name" in dct)
print (dct["name"] == name)
print(hight > age)

# Work with strings
print('**** Work with strings ****')
# 1
num_str = 125
print(type(str(num_str)))

# 2
message = 'Hi, my name is Python!'
print(message.replace('y', '0').replace('i', '1'))

# 3, 4
split_test = 'This is a split test' 
string_split = split_test.split()
string_join = ' '.join(string_split)
print(string_split, string_join)
print(len(string_join))

# Work with lists
print('**** Work with lists ****')
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)
print(list_extend.index(6))
print(len(list_extend))

# Work with dictionaries
print('**** Work with dictionaries ****')
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])
print(dict_test.keys())
print(dict_test.values())
print(dict_test.items())