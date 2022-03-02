ls1 = [3 , -2 , 5 , 16 , -7]
ls2 = ['Hello' , 'Hi' , 'guys' , 'a']

print('List 1 = ' , ls1)
print('List  = ' , ls2)

print('')

#appending list 1

print('Appending list 1: ')

newls = []
for e in ls1:
    newls.append(e + 1)

print('Adding one to each list member is: ' , newls)

print([e+1 for e in ls1])

print('')



newls = []
for e in ls1:
    newls.append(e * 10)

print('Each list member multiplied by ten is: ' , newls)

print([e * 10 for e in ls1])

print('')




newls = []
for e in ls1:
    
    newls.append(abs(e))

print('The absolute value of each list member is: ' , newls)

print([abs(e) for e in ls1])

print('')




newls = []
for e in ls1:
    if e > 0:
        e = 'Positive'
        newls.append(e)
    elif e < 0:
        e = 'Negative'
        newls.append(e)

print('Each list members state is: ' , newls)

print(['Positive' if e > 0 else 'Negative' for e in ls1])

print('')


#appending list 2

print('Appending list 2: ')

print('')

newls = []
for e in ls2:
    
    newls.append(len(e))

print('The length of each list member is: ' , newls)

print([len(e) for e in ls2])
