def sub_list(arr,target):
    result=[]
    # target=5
    for i in range(len(arr)):
        sum_list=0
        for j in range(i,len(arr)):
            sum_list+=arr[j]
            if sum_list==target:
                result.append(arr[i:j+1])
                found=True
            if not found:
                print("not in given input")
    return result
