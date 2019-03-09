summ = 0
number = 0
with open("out.txt") as f:
    for i in f:
        summ += int(i)
        number += 1

print(summ)