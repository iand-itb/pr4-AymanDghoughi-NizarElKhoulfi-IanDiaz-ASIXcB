try:
    nombres = input("Introdueix dos nombres a sumar separats per un espai: ")
    nums = nombres.split()
    resultat = 0
    while len(nums) != 2:
        nombres = input("Introdueix dos nombres a sumar separats per un espai: ")
        nums = nombres.split()

    for i in range(1, int(nums[1]) + 1):
        resultat += int(nums[0])
    print(resultat)
except Exception as e:
    if ValueError:
        print("Si us plau, introdueïx dos nombres.")
    else:
        print(e)
