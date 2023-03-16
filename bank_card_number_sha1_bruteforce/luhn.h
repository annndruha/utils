//
// Created by apmar on 10.03.2023.
//
#include "cmath"
#include <string>

int luhn_alg(std::string const & input)
{
    int check_digit = 0;
    bool odd = false;
    for (auto it = input.rbegin(); it != input.rend(); ++it)
    {
        auto digit = *it - '0';

        if ((odd = !odd))
        {
            digit *= 2;

            if (digit > 9)
                digit -= 9;
        }

        check_digit += digit;
    }

    return (check_digit * 9) % 10;
}


int luhn_alg_long(long long & input)
{
    int check_digit = 0;
    bool odd = false;

    for (short i=0; i<15; i++)
    {
        long long digit[15];
        digit[i]=input%10;
        input = input/10;

        if ((odd = !odd))
        {
            digit[i] *= 2;

            if (digit[i] > 9)
                digit[i] -= 9;
        }

        check_digit += digit[i];
    }

    return (check_digit * 9) % 10;
}