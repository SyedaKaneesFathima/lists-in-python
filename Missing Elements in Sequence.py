def missing_ele(seq):
    seq.sort()
    missing_ele= []
    for i in range(seq[0], seq[-1]):
        if i not in seq:
            missing_ele.append(i)
    return missing_ele
seq = [42,48]
missing_ele = missing_ele(seq)
print(missing_ele)  
