data = {'name': 'venkata', 
'proper': 'jammalamadugu', 
'course': 'python' , 
'details' : {'first': [25] , 'second' : [2,1,75] } }
data1 = data.get('details')

first_element = data1.get('first')

second_element = data1.get('second')

output = first_element[0] + second_element[2]
print(output) 

#second style

data1 = data['details']

output = data1['first'][0] + data1['second'][2]

print(output)

#third style

data2 = data['details']['first'][0] + data['details']['second'][2]
print(data2)

# try:
    # print(2/0)
# except:
    # print('zero division not valid')

# print(data.pop('details'))
# print(data)

# print(data.popitem())
# print(data)


