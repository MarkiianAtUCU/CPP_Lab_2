import subprocess
import os
import sys

EXECUTABLE = "/cmake-build-debug/Lab2"
EPSILON = 0.001


if len(sys.argv) !=4:
    raise Exception("Invalid call, valid call:\npython runScript.py <num of iteration> <in_file> <out_file>")

iter_num = int(sys.argv[1])
in_file = int(sys.argv[2])
out_file = int(sys.argv[3])


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

    print(f"Running C++ {len(methods)} methods {iter_num} times each:")
    print("        ALG        TIME")
    for i in methods.items():

        method_time = test_method(i[1], iter_num)
        print(f" * {i[0] + ' ' * (max(len(i[0]), 16)-len(i[0]))}   {method_time} us")


if __name__ == '__main__':
    main()
