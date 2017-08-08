l = [2, 7, 11, 15]
target = 9

def twoSum(l,target):
    l = sorted(l)
    result =[]

    for i in range(len(l)-1):
        for j in range(i+1, len(l)):
            if l[i]+l[j]==target:
                result.append((i,j))
    print(result)
twoSum(l,target)