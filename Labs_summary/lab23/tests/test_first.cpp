#include <cassert>
#include "../include/header.hpp"

void test_get_a(){
    Lol lol = Lol(10);
    auto _a = lol.get_a();
    assert(_a == 10);
}


int main(){
    test_get_a();
}