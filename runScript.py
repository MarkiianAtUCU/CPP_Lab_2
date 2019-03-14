import os
import subprocess
import datetime
import sys
import os

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


def python_process(filename):
    with open(filename, "r") as f:
        res = f.read()
    processed_list = list(map(lambda x: int(x), res.strip().split("\n")))
    summed_list = sum(processed_list)
    return summed_list, summed_list/len(processed_list)


def check_result(python_res, cpp_file_out):
    with open(cpp_file_out, "r") as f:
        res = f.read()
    cpp_res = res.strip().split("\n")
    return python_res[0] == int(cpp_res[0]) and abs(python_res[1]-float(cpp_res[1]))<=EPSILON


def test_method(method_num, n):
    res = []
    for i in range(n):
        result = subprocess.run([EXECUTABLE, method_num, in_file, out_file], stdout=subprocess.PIPE)
        res.append(int(result.stdout.decode('utf-8').strip()))
    return min(res)


methods = {"String stream": "1",
           "Atoi": "2",
           "Stoi": "3",
           "Written by hands": "4"}


def main():
    if not os.path.exists(EXECUTABLE):
        raise Exception("No executable found, consider running compilation with Cmake file")

    print("Running python script:")
    now = datetime.datetime.now()
    python_res = python_process(in_file)
    python_time = datetime.datetime.now() - now
    print(f"Python - {python_time.microseconds} us\n")

    print(f"Running C++ {len(methods)} methods {iter_num} times each:")
    print("        ALG        RESULT   TIME")
    for i in methods.items():

        method_time = test_method(i[1], iter_num)
        print(f" * {i[0] + ' ' * (max(len(i[0]), 16)-len(i[0]))} [ {'OK' if check_result(python_res, 'res.txt') else 'FAIL'} ]  {method_time} us")


if __name__ == '__main__':
    main()
