#include <iostream>
#include <string>
#include "luhn.h"
#include "sha1.hpp"
#include "vector"
#include <algorithm>
#include <cctype>
#include "sha1_to_check.h"

using namespace std;

int main() {
    string number;
    string control_digit;
    string card;
    string sha1_res;
    SHA1 sha1 = SHA1();

    // Lowercase sha1 array
    for (auto &sha: sha1_array) {
        std::transform(sha.begin(), sha.end(), sha.begin(),
                       [](unsigned char c) { return std::tolower(c); });
    }


//    std::vector<std::string> foo;
//    std::for_each(
//            __pstl::execution::par,
//            foo.begin(),
//            foo.end(),
//            [](auto&& item)
//            {
//                //do stuff with item
//            });

    // Auto-detect how many card digits missing
    int unknown_digits_len = (int) (15 - known_bin.length());
    long long max_number = 10;
    for (int i = 1; i < unknown_digits_len; i++) {
        max_number *= 10;
    }

    // Bruteforce card numbers
    cout << "Starting bruteforce for " << unknown_digits_len << " unknown digits." << endl;
    for (long long number_i = max_number; number_i < max_number * 10; number_i++) {
        number = to_string(number_i).erase(0, 1);
        if (number_i == 2 * max_number - 1) {
            break;
        }
        if (number_i % (max_number / 10) == 0) {
            cout << "Progress " << number[0] << number[1] << "%. Processed " << number << " digits." << endl;

        }

        control_digit = to_string(luhn_alg(known_bin + number)); // Get last digit
        card = known_bin + number + control_digit; // Full card number


        sha1.update(card);
        sha1_res = sha1.final();
        for (auto &sha: sha1_array) {
            if (sha1_res == sha) {
                cout << sha1_res << "\t" << card << endl;
            }
        }
    }
    return 0;
}
