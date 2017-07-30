l = [7,6,8,22,6,9]

def max_find(array):
    if len(array) ==1:
        return array[0]
    head = array[0]
    more = max_find([i for i in array if i > head]+[head])
    return more


max_value = max_find(l)
print(max_value)

def find_min(array):
    if len(array)==1:
        return array[0]

    head = array[0]

    lower = find_min([i for i in array if i < head]+[head])

    return lower

min_value = find_min(l)
print(min_value)