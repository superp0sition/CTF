#include <iostream>
#include <string>
#include <complex>
#include <algorithm>
#include <numeric>

using namespace std;

bool checkFlag(const std::string &input) {
    if (input.length() != 34)
        return false;

    if (input.substr(0, 6) != "UDCTF{")
        return false;

    if (input[6] != 'h')
        return false;

    if (input[7] - input[8] == input[9] + 15)
        return false;

    if (input[7] * input[9] != 2652)
        return false;

    if (input[7] - input[9] != 1)
        return false;

    if (input[10] != input[14])
        return false;

    if (input[14] != input[21])
        return false;

    if (input[10] != input[25])
        return false;

    if (input[21] != input[27])
        return false;

    if (std::ceil(static_cast<double>(input[10]) / 2.0) != input[12])
        return false;

    if (952 != static_cast<int>(std::pow(input[11], 2) - std::pow(input[13], 2)))
        return false;

    if (input.substr(14, 7) != "_alw4ys")
        return false;

    if (input.substr(22, 2) != input.substr(6, 2))
        return false;

    if (static_cast<int>(input[24]) % 97 != 3)
        return false;

    std::string subseq14_16 = input.substr(14, 2);
    std::string subseq26_28 = input.substr(26, 2);
    std::reverse(subseq26_28.begin(), subseq26_28.end());
    if (subseq14_16 != subseq26_28)
        return false;

    std::complex<int> c1(input[28], input[29]);
    std::complex<int> c2(76, -49);
    if (c1 != std::conj(c2))
        return false;

    int lcm_result = std::lcm(input[30], input[31]);
    if (lcm_result != 6640)
        return false;

    if (input[30] <= input[31])
        return false;

    if (input[32] != (input[31] + input[30] - input[24]))
        return false;

    if (input[33] != '}')
        return false;

    return true;
}

int main() {
    if (checkFlag("UDCTF{h4v3_y0u_alw4ys_h4d_a_L1SP?}"))
        std::cout << "Flag is valid!" << std::endl;
    else
        std::cout << "Flag is not valid!" << std::endl;

    return 0;
}
