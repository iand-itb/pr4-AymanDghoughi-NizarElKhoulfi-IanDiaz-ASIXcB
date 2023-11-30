""""
Ayman Dghoughi, Ian Díaz, Nizar ElK
30/11/2023
M03 UF1 pp4
Descripció: Programa que mostra un triangle amb nombres a les cantonades.
"""

alçada = int(input("Donam una alçada entre el 2 i el 9: "))
count = 0
for i in range(1, alçada + 1):
    print(i * count)
    count += 1

