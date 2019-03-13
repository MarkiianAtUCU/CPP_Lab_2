import random


def write_randint(n_rows, path, from_to=(-1073741, 1073741)):
    with open(path, "w") as f:
        for i in range(n_rows):
            f.write(f"{random.randint(*from_to)}\n")


write_randint(100000, "./out.txt")
