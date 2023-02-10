#include "../include/header.hpp"

Lol::Lol(int _a): some_smart_word(_a){}

Lol::~Lol(){
    delete this->string;
}

int Lol::get_some_smart_word() const {
    return some_smart_word;
}

char* Lol::get_string() const {
    return this->string;
}