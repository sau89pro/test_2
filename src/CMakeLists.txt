cmake_minimum_required(VERSION 2.8)

project(Test)

set(CMAKE_INSTALL_PREFIX ${CMAKE_BINARY_DIR}/../install)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(test test.cpp)

target_link_libraries(test ${CONAN_LIBS})

install(TARGETS test)