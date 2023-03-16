cmake_minimum_required(VERSION 3.24)
project(sha1_bank_cards)

set(CMAKE_CXX_STANDARD 17)

add_executable(sha1_bank_cards main.cpp sha1.hpp luhn.h sha1_to_check.h)
