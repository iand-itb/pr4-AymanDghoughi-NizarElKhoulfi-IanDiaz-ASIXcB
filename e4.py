BLANC = "██"
NEGRE = "  "
for i in range(1, 9):
    for j in range(1, 9):
        if (i + j) % 2 == 0:
            print(NEGRE, end="")
        else:
            print(BLANC, end="")
        #print(" ", end="")
    print()
