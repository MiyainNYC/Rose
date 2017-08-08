l = [-1, 0, 1, 2, -1, -4]


def threeSum(l):
    l = sorted(l)
    result =[]

    for i in range(len(l)-2):
        begin = i+1
        print(begin)
        end = len(l)-1

        while end>begin:
            cur_sum = l[i]+l[begin]+l[end]
            if cur_sum == 0:
                result.append((l[i],l[begin],l[end]))
                begin +=1
                end -=1
            elif cur_sum<0:
                begin +=1
            else:
                end-=1
    return set(result)

r = threeSum(l)
print(r)

S = [-1, 2, 1, -4]
T = 1


