S = [-1,2,1,-4]

T = 1

def app3sum(S,T):

    i = 0
    j = 1
    diff = abs(S[i] + S[j] + S[j + 1] - T)
    result = S[i] + S[j] + S[j + 1]
    for i in range(len(S)):
        for j in range(1,len(S)-1):
            if abs(S[i]+S[j]+S[j+1]-T)<diff:
                diff = abs(S[i]+S[j]+S[j+1]-T)
                result = S[i]+S[j]+S[j+1]
    print(result)

app3sum(S,T)