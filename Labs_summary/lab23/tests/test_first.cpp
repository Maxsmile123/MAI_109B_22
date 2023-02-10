#include <cassert>
#include "../include/header.hpp"

void test_get_some_smart_word(){
    Lol lol = Lol(10);
    auto _a = lol.get_some_smart_word();
    assert(_a == 10);
}


int main(){
    test_get_some_smart_word();
    return 0;
    
}