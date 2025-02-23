l1=['a','b','c','d','e','f','g']
l2=['u','z']
result=[]
for i in range(len(l2)):
    result.append(l1[i]+l2[i])
result.extend(l1[len(l2):])
print(*result)
