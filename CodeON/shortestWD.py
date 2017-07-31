words = ["practice", "makes", "perfect", "coding", "makes"]

def shortest_d(word1,word2):

    dict_w = dict()
    for i,j in enumerate(words):
        dict_w[j] = i
    print(abs(dict_w[word1]-dict_w[word2]))

shortest_d('perfect','makes')