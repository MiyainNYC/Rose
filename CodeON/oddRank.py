l = [1,2,3,4,5]

def odd_r(l):
    odd = [j for i,j in enumerate(l) if i%2==0]
    not_odd = [j for i,j in enumerate(l) if i%2!=0]
    print(odd+not_odd)

odd_r(l)