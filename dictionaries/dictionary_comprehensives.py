numbers = [1,3,5,7,9,11]
#{1:1,3:9,5:25,7:49,9:81,11:121}
data1 = {}
for i in numbers:
    data1[i] = i**2

print(data1) 

print({i:i**2 for i in numbers})
    
    
    