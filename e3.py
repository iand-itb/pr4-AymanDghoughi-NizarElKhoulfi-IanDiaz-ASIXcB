try:
    num = int(input())
    sumaParells = 0
    sumaSenars = 0

    for i in range(num):
        if i % 2 == 0:
            sumaParells += i
        else:
            sumaSenars += i
    print(sumaParells)
    print(sumaSenars)
except Exception as e:
    if ValueError:
        print("Si us plau, introdueix només nombres enters.")
    else:
        print(e)
