import os
import time
import sys
import filecmp


def runFile(times, inFile, outFile):
    os.system("./Lab2 1 {} {}".format(inFile, outFile))
    with open("../{}".format(outFile)) as f:
        lines = f.read().splitlines()
    start = time.time()
    for i in range(1, 3):
        for _ in range(times):
            os.system('./Lab2 {} {} {}'.format(i, inFile, outFile))
        with open("../{}".format(outFile)) as f:
            perm = f.read().splitlines()
            if lines != perm:
                print("Not same result")
                return 0
    print(time.time() - start)

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