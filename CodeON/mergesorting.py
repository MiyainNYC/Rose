list_a = [3,6,88,9,2]
list_b = [4,6,7,9,11]

def mergesorting(list_a, list_b):
    i = 0
    j = 0
    k = 0
    merged_list = [None]*(len(list_a)+len(list_b))
    while i < len(list_a) and j < len(list_b):
        if list_a[i] < list_b[j]:
            merged_list[k] = list_a[i]
            i = i + 1
        else:
            merged_list[k] = list_b[j]
            j = j + 1
        k = k + 1
    while i < len(list_a):
        merged_list[k] = list_a[i]
        i = i + 1
        k = k + 1

    while j < len(list_b):
        merged_list[k] = list_b[j]
        j = j + 1
        k = k + 1
    print(merged_list)

mergesorting(list_a, list_b)