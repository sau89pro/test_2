#include "test_lib_1.h"
#include "test_lib_2.h"
#include <iostream>

void func()
{
   std::cout << "func" << '\n';
}

int main()
{
   test_lib_1();
   
   func();
   
   test_lib_2();
   
   return 0;
}
