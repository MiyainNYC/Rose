s = "the sky is blue"

def reversed(s):
    list_s = s.split(' ')
    result = []
    for i in list_s:
        result.insert(0,i)

    print(' '.join(result))

reversed(s)


s2 = "Let's take LeetCode contest"

def reverse_2(s2):
    string = s2.split(' ')
    result = []
    for i in string:
        r = []
        for j in i:
            r.insert(0,j)
        result.append(''.join(r))
    print(' '.join(result))
reverse_2(s2)
