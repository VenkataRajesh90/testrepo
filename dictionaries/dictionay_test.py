data = {'name': 'venkata', 'proper': 'jammalamadugu', 'course': 'python'}
#       'key' : 'value'  , 'key'   : 'value', 'key'   : 'value'
print(type(data))
print(dir(data))


data = {'name': 'venkata', 'proper': 'jammalamadugu', 'course': 'python'}
data1 = {}
for i,j in data.items():
    data1[j] = i
print(data1)

data = {'name': 'venkata', 'proper': 'jammalamadugu', 'course': 'python'}

for i,j in data.items():
    if i == 'proper':
        data[i] = 'jmd'
print(data)