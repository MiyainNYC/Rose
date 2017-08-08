S = [-1, 0, 1, 2, -1, -4]

def threeSum(S):
    S = sorted(S)
    print(S)

    i = 0
    while S[i]<=0 and i<=(len(S)-1):
        if S[i]+S[i+1] <= 0:
            for j in range(i+2,len(S)):
                if S[i]+S[i+1]+S[j]==0:
                    print(S[i],S[i+1],S[j])
        i +=1

threeSum(S)


