# new_list = [new_item in item in list if test]
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}


# num = [1, 2, 3]
# new_list = [n+1 for n in num]
# print (new_list)


# names = ["Alex", "Beth", "Eleanor", "Caroline", "Charlie"]
# new = [i.upper() for i in names if len(i)>4]
# print (new)

# numbers = [1, 1, 2, 3, 5, 4, 6, 8, 34, 55]
# new_num= [n for n in numbers if n%2==0]
# print (new_num)

name = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
score = [88, 66, 87, 90, 76, 78]
new_dict = {name[i]:score[i] for i in range(len(name))}
print (new_dict)

passed_students = {key:value for key,value in new_dict.items() if value>80}
print (passed_students)