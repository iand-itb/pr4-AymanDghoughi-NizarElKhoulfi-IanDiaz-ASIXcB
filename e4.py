BLANC = "██"
NEGRE = "  "
for i in range(1, 9):
    for j in range(1, 9):
        if (i + j) % 2 == 0:
            print(BLANC, end="")
        else:
            print(NEGRE, end="")
        #print(" ", end="")
    print()
