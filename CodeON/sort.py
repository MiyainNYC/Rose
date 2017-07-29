l = [3,4,88,1,4,5,0,3]

## divide and conquer
def qsort(array):
    if len(array) < 2:
        return array
    head, *tail = array
    less = qsort([i for i in tail if i < head])
    more = qsort([i for i in tail if i >= head])
    return less+[head]+more


def sort_list(l):
    sorted_list = [None]*len(l)
    leng = len(l)
    s = 0
    e = len(l)-1

    while leng>0 and e>s:
        min = l[0]
        max = l[-1]
        for i in range(leng):
            if l[i]<min:
                min = l[i]
            if l[i]>max:
                max = l[i]
        sorted_list[s] = min
        sorted_list[e] = max

        leng -=2
        l.remove(min)
        l.remove(max)
        s +=1
        e-=1
    print(sorted_list)

l = qsort(l)
print(l)





