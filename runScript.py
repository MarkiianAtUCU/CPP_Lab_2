import os
import subprocess
import time
import sys

EXECUTABLE = "./cmake-build-debug/Lab2.exe"


def process_python(path):
    sum = 0
    counter = 0
    with open(path) as f:
        for i in f:
            counter += 1
            sum += int(i)
    print(sum, '%.2f' % sum/counter)

# def runFile(times, inFile, outFile):
#     os.system("./Lab2 1 {} {}".format(inFile, outFile))
#     with open("../{}".format(outFile)) as f:
#         lines = f.read().splitlines()
#     for i in range(1, 3):
#         totalTime = 0
#         for _ in range(times):
#             os.system('./Lab2 {} {} {}'.format(i, inFile, outFile))
#             with open("../{}".format(outFile)) as f:
#                 perm = f.read().splitlines()
#                 totalTime += int(perm[2])
#                 if lines[:1] != perm[:1]:
#                     print("Not same result")
#                     return 0
#         print("{} is {}".format(i, totalTime))
#

def main():
    # if len(sys.argv) != 4:
    #     print("Wrong number of arguments!")
    #     raise Exception("Wrong number of arguments")
    res=[]
    process_python("in.txt")
    for i in range(100):
        result = subprocess.run([EXECUTABLE, "2", "in.txt", "res.txt"], stdout=subprocess.PIPE)
        res.append(int(result.stdout.decode('utf-8').strip()))
    print(sum(res))


    # print(sys.argv)
    # runFile(int(arguments[1]), arguments[2], arguments[3])


if __name__ == "__main__":
    main()
