import os
import time
import sys

transformations = ["StringStream", "Atoi", "Stoi", "Own function"]

def runFile(times, inFile, outFile):
    print("Processing data, microseconds:")
    os.system("./Lab2 1 {} {}".format(inFile, outFile))
    with open("../{}".format(outFile)) as f:
        lines = f.read().splitlines()
    for i in range(1, 5):
        minimum = float('+inf')
        for _ in range(times):
            start = time.time()
            os.system('./Lab2 {} {} {}'.format(i, inFile, outFile))
            result = time.time() - start
            if result < minimum:
                minimum = result
        with open("../{}".format(outFile)) as f:
            perm = f.read().splitlines()
            if lines[:2] != perm[:2]:
                print("Not same results")
                return 0
        print("{}: {}".format(transformations[i-1], round(minimum*10**6)))
    print("All results are the same")

def main():
    if len(sys.argv) != 4:
        print("Wrong number of arguments!")
        raise Exception("Wrong number of arguments")

    if os.path.isdir('build'):
        os.chdir('build')
    else:
        os.system('mkdir build')
        os.chdir('build')
        os.system('cmake -G"Unix Makefiles" ..')
        os.system('make')
    arguments = sys.argv
    runFile(int(arguments[1]), arguments[2], arguments[3])


if __name__ == "__main__":
    main()