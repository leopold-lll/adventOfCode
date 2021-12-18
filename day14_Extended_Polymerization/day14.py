#read input
fin = open("in.txt", 'r') # "in.txt" "inEx.txt"
seq = fin.readline().strip("\n")
fin.readline() #discard empty

# store rules
rules = {}
lettersList = []
for l in fin:
    b,a,p = l[0], l[1], l[6] #before, after, product
    lettersList.append(b)
    # each rules is: key (input seq) -> [out_left, out_right, actual_occ, new_occ]
    rules.update({"".join([b,a]): ["".join([b,p]), "".join([p,a]), 0, 0]})

# store initial input of seq
for i in range(len(seq)-1):
    rules["".join([seq[i], seq[i+1]])][2] +=1
print(rules, "\n")

#apply rules
steps=40
for s in range(steps):
    #virtual update
    for _, v in rules.items():
        rules[v[0]][3] += v[2]
        rules[v[1]][3] += v[2]

    #physical update
    for k, v in rules.items():
        #k&v sono link agli riferimenti agli elementi e non copie!
        v[2] = v[3]
        v[3] = 0
    # print(rules, "\n")

#compute occurrencies
lettersSet = set(lettersList)
letters = dict.fromkeys(lettersSet, 0)
#manage corner case (left and right side of seq)
letters[seq[0]] += 1
letters[seq[-1]] += 1

for k, v in rules.items(): #count
    letters[k[0]] += v[2]
    letters[k[1]] += v[2]

for k, v in letters.items(): #divide by 2 (I was considering couple not single)
    letters[k] = int(v/2)
print(letters)
print("The difference after", steps, "is:", max(letters.values()) - min(letters.values()))
