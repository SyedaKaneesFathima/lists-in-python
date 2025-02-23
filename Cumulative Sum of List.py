nums=list(map(int,input().split()))
result=[]
count=0
for num in nums:
    count+=num
    result.append(count)
print(result)   
