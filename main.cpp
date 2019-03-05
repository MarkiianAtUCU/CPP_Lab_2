#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>
using std::vector;
using std::string;

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

int main() {
    vector< string> input_nums = read_file("../out.txt");
    std::cout << "Hello, World!" << std::endl;
    std::string word;

    return 0;
}