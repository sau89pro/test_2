from conans import ConanFile, CMake, tools

class TestConan(ConanFile):
    name = "test"
    version = "2.0"
    description = "The project for conan-based build setup testing"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    requires = "test_lib_1/1.0@sau/demo", "test_lib_2/1.0@sau/demo"
    exports_sources = "src*"
    generators = "cmake"
    no_copy_source = True

    def source(self):
        tools.replace_in_file("src/CMakeLists.txt", "project(Test)",
                              '''project(Test)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')
        tools.replace_in_file("src/CMakeLists.txt", "add_executable(test test.cpp)",
                              '''add_executable(test test.cpp)

target_link_libraries(test ${CONAN_LIBS})''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()
        cmake.install()
    
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

