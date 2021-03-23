@echo off

set SCRIPT_DIR=%~dp0

cd /d %SCRIPT_DIR%

if not exist build mkdir build
if not exist install mkdir install

cd build

conan install ..
conan build -pf ../install ..
