#include <iostream>
#include <fstream>
#include <chrono>
#include <atomic>
#include <sstream>
#include <vector>
#include <cstring>
#include <stdexcept>
#include <functional>
#include <cmath>
#include <iomanip>
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


vector<int> transform(const vector<string>& numbers, std::function<int (string)> const &f) {
    vector<int> output;
    output.reserve(numbers.size());

    for (auto const & element:numbers) {
        output.push_back(f(element));
    }
    return output;
}

int trStringStream(const string& str) {
    std::stringstream parser;
    parser << str;
    int x = 0;
    parser >> x;
    return x;
}

int trAtoi(string in) {
    return std::atoi(in.c_str());
}

int trStoi(string str) {
    return std::stoi(str);
}

int trHand(string str) {
    int counter = static_cast<int>(str.length());
    int res = 0;
    for (auto &c:str) {
        counter -=1;
        if (c!='-') {
            res += (c - '0') * static_cast<int>(std::pow(10, counter));
        }
    }
    if (str[0]=='-'){
        return -res;
    }
    return res;
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

void process_and_write(string filename,std::vector<int> numbers) {
    std::ofstream file;
    file.open (filename);
    int sum = 0;
    for (auto &num:numbers){
        sum+=num;
    }

    std::stringstream ss;
    ss << std::fixed << std::setprecision(2) << (float)sum / (float)numbers.size();

    file << sum << std::endl;
    file << ss.str() << std::endl;
}


int main(int argc, char *argv[]) {

    if (argc != 4) {
        std::cout << "Wrong number of files!" << std::endl;
        std::cout << "The format is following: <number of method> <input file> <output file>" << std::endl;
        return 1;
    }

    std::vector<string> numbers = read_file(std::string("../") + std::string(argv[2]));

    if (numbers.empty()) {
        std::cout<<"Error, file is empty"<<std::endl;
        return 1;
    }
    std::vector<int> out;
    auto start = get_current_time_fenced();


    switch (argv[1][0]) {
        case '1':
            out = transform(numbers, trStringStream);;
            break;
        case '2':
            out = transform(numbers, trAtoi);;
            break;
        case '3':
            out = transform(numbers, trStoi);;
            break;
        case '4':
            out = transform(numbers, trHand);;
            break;
        default:
            std::cout<<"Only 1 - 4 algorithms allowed"<<std::endl;
            return 1;
    }

    auto end = get_current_time_fenced();
    long long time = to_us(end - start);

    process_and_write(std::string("../") + std::string(argv[3]), out);

    return 0;
}