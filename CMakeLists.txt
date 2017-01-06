cmake_minimum_required(VERSION 3.6)
project(pyhog)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED on)

find_package(PythonLibs 2.7 REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})

#find_package(OpenCV 3.1 REQUIRED)
#include_directories( ${OpenCV_INCLUDE_DIRS} )

#find_package(Armadillo 7.600 REQUIRED)
#include_directories(${ARMADILLO_INCLUDE_DIRS})

#set(Boost_REALPATH ON)
#set(BOOST_USE_STATIC_LIBS OFF)
#set(BOOST_USE_MULTITHREADED ON)
#set(BOOST_USE_STATIC_RUNTIME OFF)

#set(BOOST_ROOT "/usr/")
#FIND_PACKAGE(Boost 1.62)

#add_definitions(-DBOOST_ALL_DYN_LINK)
#include_directories(${Boost_INCLUDE_DIRS})
#link_directories(${Boost_LIBRARY_DIRS})


#file(GLOB PYHOG_SRC "pyhog/*.hpp" "pyhog/*.cpp")
add_library(pyhog "pyhog/pyhog_impl.hpp" "pyhog/pyhog_impl.cpp")
