#include <iostream>
#include <fstream>
#include <chrono>
#include <atomic>
#include <sstream>
#include <string>
#include <vector>
#include <cstring>
#include <stdexcept>
using std::vector;
using std::string;


inline std::chrono::high_resolution_clock::time_point get_current_time_fenced()
{
    std::atomic_thread_fence(std::memory_order_seq_cst);
    auto res_time = std::chrono::high_resolution_clock::now();
    std::atomic_thread_fence(std::memory_order_seq_cst);
    return res_time;
}


template<class D>
inline long long to_us(const D& d) {
    return std::chrono::duration_cast<std::chrono::microseconds>(d).count();
}

std::vector<int> transformStringStream(std::vector<string> numbers) {
    vector<int> output;
    for (int i = 0; i < numbers.size(); ++i) {
        std::stringstream parser;
        parser << numbers[i];
        int x = 0;
        parser >> x;
        output.push_back(x);
    }
    return output;
}

std::vector<int> transformAtoi(std::vector<string> numbers) {
    vector<int> output;
    for (int i = 0; i < numbers.size(); ++i) {
        const char *c = numbers[i].c_str();
        int x = std::atoi(c);
        output.push_back(x);
    }
    return output;
}

vector<string> read_file(string const &path) {
    vector<string> res;
    string num_1;

    std::ifstream file(path);
    if (file.is_open()) {
        while (file >> num_1) {
            res.push_back(num_1);
        }
        file.close();
    } else {
        throw std::invalid_argument( "File not found" );
    }
    if (res.empty()) {
        throw std::invalid_argument("File is empty");
    }
    return res;
}

int main(int argc, char *argv[]) {

    if (argc != 4) {
        std::cout << "Wrong number of files!" << std::endl;
        std::cout << "The format is following: ./stringToInt <number of method> <input file> <output file>";
        return 1;
    }

    std::vector<string> numbers;

    numbers = read_file(std::string("../") + std::string(argv[2]));
    if (numbers.size() == 0) {
        return 1;
    }
    std::vector<int> out;
    auto start = get_current_time_fenced();
    switch (argv[1][0] - '0') {
        case 1:
            out = transformStringStream(numbers);
            break;
        case 2:
            out = transformAtoi(numbers);
            break;
    }
    auto end = get_current_time_fenced();

    std::cout << "Time = " << to_us(end - start) << std::endl;

    return 0;
}