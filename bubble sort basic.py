list = [9, 8, 7, 6, 4, 5, 2, 3, 1]

length = len(list)
for i in range(length):
    for j in range(0 , length-i-1):
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]



            print(list)