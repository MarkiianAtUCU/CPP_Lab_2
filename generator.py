import random
def write_randint(n_rows, path, from_to=(-1073741, 1073741)):
    with open(path, "w") as f:
        for i in range(n_rows):
            f.write(f"{random.randint(*from_to)}\n")

<<<<<<< HEAD
write_randint(100000, "./out.txt")
=======
write_randint(100000, "./in.txt")
>>>>>>> f7c591857b0db73fb1fc31535363100966e0ebcd
