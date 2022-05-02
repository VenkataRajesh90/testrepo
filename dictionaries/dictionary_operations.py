#data = {'name': 'venkata', 'proper': 'jammalamadugu', 'course': 'python'}
data = {'name': 'venkata', 'proper': 'jammalamadugu', 'course': 'python' , 'proper' : 'kadapa'}
print(data.keys())
print(data.values())

#style1
print(data.get('name'))
print(data.get('course'))
print(data['name'])

#style2
print(data['proper'])

friends = {'a' : 100, 'b' : 200, 'c' : 300 }
for i in friends:
    print(i,':',friends[i],end = ' ')
    
data = {'name': 'venkata', 'proper': 'jammalamadugu'}
data1 = {'proper': 'jammalamadugu', 'name': 'venkata'}

print(data == data1)
print(data != data1)

data = {'name': 'venkata', 'proper': 'jammalamadugu', 'course': 'python'}

print(data.clear())

data = {'name': 'venkata', 'proper': 'jammalamadugu', 'course': 'python' , 'details' : {'first': [25] , 'second' : [2,1,75] } }
#100
# pop popitem

data1 = data.get('details')
print(data1)

first_element = data1.get('first')
print(first_element)

second_element = data1.get('second')
print(second_element)

output = first_element[0] + second_element[2]
print(output)


data.pop('details')
print(data)

print(data.popitem())
print(data)

data = {'name': 'venkata', 'proper': 'jammalamadugu', 'course': 'python',
       'details' : {'first': [25] , 'second' : [2,1,75] } }

data1 = {'venkata':'name','pro':'jmd'}

data.update(data1)

print(data)

name = [1,2,3,4,5,6]
print({}.fromkeys(name,10))









    
