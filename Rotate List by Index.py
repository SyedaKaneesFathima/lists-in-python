list=[1,2,3,4,5]
index=6
index=index%len(list)   
result=list[index:]+list[:index]
print(result)
