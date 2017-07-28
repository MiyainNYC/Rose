colors = [0,1,2,1,1,0,0,2,2]

def sort_colors(colors):
    i = 0
    j = 0
    k = 0

    for color in colors:
        if color ==0:
            i+=1
        if color ==1:
            j+=1
        if color ==2:
            k+=1

    for red in range(i):
        colors[red] = 0
    for green in range(i, i+j):
        colors[green] = 1
    for blue in range(i+j,i+j+k):
        colors[blue]  =2
    print(colors)

sort_colors(colors)