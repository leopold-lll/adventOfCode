import re


def read_input(file_name="sample.txt"):
    with open(file_name) as fin:
        matCore = [list(line.strip()) for line in fin]

    # Determinare la lunghezza di una riga
    D = len(matCore[0]) + 2
    # Aggiungere il contorno
    contorno = ['.'] * D
    matFull = [contorno]
    for riga in matCore:
        # Riga con contorno laterale
        matFull.append(['.'] + riga + ['.'])
    # Contorno inferiore
    matFull.append(contorno)
    return matFull


def count_pattern(v, pattern="XMAS"):
    return len(re.findall(pattern, v)) + len(re.findall(pattern[::-1], v))


def collapse_horizontally(mat):
    return "".join([cell for row in mat for cell in row])


def collapse_vertically(mat):
    # zip(*mat) clever method to rotate the matrix!
    return "".join([cell for col in zip(*mat) for cell in col])


def collapse_diagonally(mat):
    v = []
    D = len(mat)  # Dimensione della matrice
    # print("\nTriangolo alto")
    for i in range(D):
        for j in range(i + 1):
            # print(j, i - j)
            v.append(mat[j][i-j])

    # Se la matrice non fosse quadrata bisognerebbe aggiungere qui una sezione
    # print("\nTriangolo basso")
    # Il triangolo basso segue la stessa logica di quello alto ma sottraendo le cordinate a (D-1)
    for i in range(D-1):
        for j in range(i + 1):
            # print((D-1)-j, (D-1)-(i - j))
            v.append(mat[(D-1)-j][(D-1)-(i - j)])

    return ("".join(v))


def collapse_diagonally_back(mat):
    v = []
    D = len(mat)  # Dimensione della matrice
    # print("\nTriangolo basso")
    for i in range(D):
        for j in range(i + 1):
            # print((D-1)-j, i - j)
            v.append(mat[(D-1)-j][i-j])

    # print("\nTriangolo alto")
    for i in range(D-1):  # -1 perché salto la diagonale principale
        for j in range(i + 1):
            # print(j, (D-1)-(i - j))
            v.append(mat[j][(D-1)-(i - j)])
    return ("".join(v))


def part1(mat):
    # La logica di base consiste nel creare una stringa di lettura per ognuna delle 4 direzioni
    occ = 0
    occ += count_pattern(collapse_horizontally(mat))
    occ += count_pattern(collapse_vertically(mat))
    occ += count_pattern(collapse_diagonally(mat))
    occ += count_pattern(collapse_diagonally_back(mat))
    print("Part1 - Le occorrenze di XMAS  sono:", occ)


def part2(mat):
    # È richiesta una logica completamente diversa...
    # Bisogna ragionare in maniera spaziale (Forse è più facile!)
    # Per ogni A cercherò le M e S associate! (in ognuna delle 4 direzioni!)
    # M.S
    # .A.
    # M.S
    occ = 0
    for i in range(1, len(mat)-1):
        for j in range(1, len(mat)-1):
            if mat[i][j] == "A" and (
                    (mat[i+1][j+1] == "M" and mat[i+1][j-1] == "M" and mat[i-1][j+1] == "S" and mat[i-1][j-1] == "S") or
                    (mat[i-1][j+1] == "M" and mat[i-1][j-1] == "M" and mat[i+1][j+1] == "S" and mat[i+1][j-1] == "S") or
                    (mat[i+1][j+1] == "M" and mat[i-1][j+1] == "M" and mat[i+1][j-1] == "S" and mat[i-1][j-1] == "S") or
                    (mat[i+1][j-1] == "M" and mat[i-1][j-1] == "M" and mat[i+1][j+1] == "S" and mat[i-1][j+1] == "S")):
                # print("Found at: ", i, j)
                occ += 1
    print("Part2 - Le occorrenze di X-MAS sono:", occ)


if __name__ == "__main__":
    matFull = read_input("input.txt")
    part1(matFull)
    part2(matFull)
