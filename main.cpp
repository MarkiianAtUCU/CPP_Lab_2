#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>

std::vector<std::pair<std::string,std::string>> read_file(std::string const &path) {
    std::vector<std::pair<std::string,std::string>> res;
    std::string num_1, num_2;

    std::ifstream file(path);
    if (file.is_open()) {
        while (file >> num_1 >> num_2) {
            std::pair<std::string, std::string> value_pair(num_1, num_2);
            res.push_back(value_pair);

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
    std::vector<std::pair<std::string, std::string>> input_nums = read_file("../out.txt");
    std::cout << "Hello, World!" << std::endl;
    std::string word;

    return 0;
}