#include "../include/header.hpp"

Lol::Lol(int _a): a(_a){}

Lol::~Lol(){
    delete this->string;
}

int Lol::get_a() const {
    return a;
}

char* Lol::get_string() const {
    return this->string;
}