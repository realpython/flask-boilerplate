with open('BaseCases.txt','r') as inf:
    dict_from_file = eval(inf.read())
print(type(dict_from_file))

dict_from_file["120000 people were injured"] = "1500 people were injured"

print(dict_from_file)
new_dict = open("BaseCases.txt", 'w')
new_dict.write(str(dict_from_file))
new_dict.close()
