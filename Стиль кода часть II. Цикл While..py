my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

s = [len(my_list) - 1]
print(s)

index = 0

while len(my_list) > index:

    if my_list[index] < 0:
        break

    if my_list[index] > 0:
        print(my_list[index])

    index += 1