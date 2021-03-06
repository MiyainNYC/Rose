l = [7,6,8,22,6,9]

def max_find(array):
    if len(array) ==1:
        return array[0]
    head = array[0]
    more = max_find([i for i in array[1:] if i > head]+[head])
    return more


max_value = max_find(l)
print(max_value)

def find_min(k,array):
    if len(array)<=k:
        return array

    head = array[0]

    lower = find_min(k,[i for i in array[1:] if i < head])
    higher =find_min(k,[i for i in array[1:] if i > head])

    return list(lower+[head]+higher)[:k]

min_value = find_min(3,l)
print(min_value)