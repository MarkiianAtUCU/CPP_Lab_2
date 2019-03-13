import os
import subprocess
import time
import sys

EXECUTABLE = "/cmake-build-debug/Lab2"

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
#
# def python_check(filename):
#     with open(filename, "r") as f:
#         f.read()
#         print(f)

result = subprocess.run([EXECUTABLE, "1", "in.txt", "out.txt"], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
# result = subprocess.run(["dir"], shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
print(result)
# python_check("in.txt")
# if len(sys.argv) != 4:
#     print("Wrong number of arguments!")
#     raise Exception("Wrong number of arguments")



