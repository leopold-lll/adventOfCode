
#read input
new_pts = []
folds = []
f = "in.txt" # "in.txt" "inExample.txt"
with open(f) as fin:
    for l1 in fin:
        if l1=="\n":
            break
        x, y = l1.strip("\n").split(",")
        new_pts.append((int(x), int(y)))

    for l2 in fin:
        side, line = l2.strip("\n").split(" ")[-1].split("=")
        folds.append([0 if side=="x" else 1, int(line)])

pts = set(new_pts)
print("\npoints len", len(pts))#, ":", pts)

#start folding
for s, l in folds: #side & line
    print("\tFold on side", s, "on line", l)
    new_pts = []
    ll = 2*l
    for pt in pts:
        if pt[s] < l:
            new_pts.append(pt)
        elif pt[s] > l:
            new_pt = (ll-pt[0], pt[1]) if s==0 else (pt[0], ll-pt[1]) #fold the point
            # print("\tGenerate", new_pt, "from", pt)
            new_pts.append(new_pt)
    pts = set(new_pts)
    print("\npoints len", len(pts))#, ":", pts)

#print code
import numpy as np
mat = np.zeros((40, 10), dtype=int)
for pt in pts:
    mat[pt[0], pt[1]] = 1

for y in range(10):
    for x in range(40):
        print("@" if mat[x,y]==1 else " ", end='')
    print()

