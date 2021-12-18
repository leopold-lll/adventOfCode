def cost(cave, y, x):
    return cave[y][x][1] if x>=0 and y>=0 else 9999999999999999999999999

def printCave(cave, costOnly):
    for r in cave:
        if costOnly:
            for v in r:
                print(v[0], end="")
            print()
        else:
            print(r)

def computePathCost(cave):
    # printCave(cave, True)
    for y in range(len(cave)):
        for x in range(len(cave[y])):
            
            #corner case (should be skipped)
            if y==0 and x==0:
                continue

            #update support values
            p = cave[y][x]  #create a reference
            left, up = [cost(cave,y,x-1), cost(cave,y-1,x)]
            if left<up:
                p[1] = left + p[0]
                p[2], p[3] = x-1, y
            else:
                p[1] = up + p[0]
                p[2], p[3] = x, y-1

    # printCave(cave, False)
    print("The cost of shortest path is:", cave[-1][-1][1])

def computePath(cave):
    path=[]
    p=[0, 0, len(cave)-1, len(cave[0])-1]
    while p[2]!=-1 and p[3]!=-1:
        path.append((p[2], p[3]))
        p = cave[p[3]][p[2]]

    path.reverse()
    print("Path:", path)


if __name__=="__main__":
    #read input
    fin = open("in.txt", 'r') # "in.txt" "inEx.txt"

    cave = [] #x*y: [local_cost, path_cost, paren_x, parent_y)]
    for line in fin:
        row = []
        for c in line.strip("\n"): #cost
            row.append( [int(c), 0, -1, -1] )
        cave.append(row)

    #quintuplicate(N) the map
    N=5
    X = len(cave[0])
    Y = len(cave)
    caveXN = [[[0]*4 for i in range(N*X)] for i in range(N*Y)]

    for yN in range(N):
        YN=yN*Y
        for xN in range(N):
            XN=xN*X
            for y in range(len(cave)):
                for x in range(len(cave[y])):
                    v = (cave[y][x][0] +yN +xN)
                    caveXN[YN+y][XN+x][0] = (v-1)%9 +1 #strange module operation


    cave[0][0] = [0, 0, -1, -1] #set the initial point at no cost
    computePathCost(cave)
    computePath(cave)

    caveXN[0][0] = [0, 0, -1, -1] #set the initial point at no cost
    computePathCost(caveXN)
    # computePath(caveXN)







