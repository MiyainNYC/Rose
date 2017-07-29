S = [1, 0, -1, 0, -2, 2]

target = 0

def fourSum(S,target):
    S = sorted(S)
    i = 0
    j = 1

    while i<len(S)-2:
        if S[i]+S[j]<=0:
            for k in range(j+1,len(S)):
                if S[i]+S[j]+S[k]<=0:
                    for m in range(k+1,len(S)):
                        if S[i]+S[j]+S[k]+S[m] ==0:
                            print(S[i],S[j],S[k],S[m])

        i+=1
        j+=1

fourSum(S,target)


