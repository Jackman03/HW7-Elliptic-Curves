#!/bin/bash

#Not my code, just coppied from someone in class
#Shoutout to tutturu on discord
# Define relative directories
INPUT_DIR="$(dirname "$0")/testCases/in/"
OUTPUT_DIR="$(dirname "$0")/testCases/out/"

# Check if the argument is provided
if [ -z "$1" ]; then
    echo "No source file provided."
    echo "Usage: $0 <source_file>"
    exit 1
fi

# Compile or set execution command based on the source file
case $1 in
    ecpoints.cpp)
        rm -f -- a.out
        g++ primrootcheck.cpp
        if [ $? -ne 0 ]; then
            echo "Compilation of ecpoints.cpp failed."
            echo "Goodbye!"
            exit 1
        fi
        EXE="./a.out"
        ;;
    ecpoints.java)
        rm -f -- primrootcheck.class
        javac primrootcheck.java
        if [ $? -ne 0 ]; then
            echo "Compilation of ecpoints.java failed."
            echo "Goodbye!"
            exit 1
        fi
        EXE="java ecpoints"
        ;;
    ecpoints.py)
        EXE="python3 ecpoints.py"
        ;;
    *)
        echo "Invalid source file name."
        echo "-> should be ecpoints.cpp, ecpoints.java, or ecpoints.py"
        exit 1
        ;;
esac

echo "Compilation of $1 succeeded."

# Check if input directory exists
if [ ! -d "$INPUT_DIR" ]; then
    echo "Input directory $INPUT_DIR does not exist."
    exit 1
fi

# Check if output directory exists
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "Output directory $OUTPUT_DIR does not exist."
    exit 1
fi

# Loop through all sample test cases and generate outputs
for i in $(ls "$INPUT_DIR"); do
    echo "Attempting test case: $i"
    # Generate the output for the current test case
    eval $EXE < "$INPUT_DIR$i" > "myoutput_$i"
    # Construct the expected output file name (e.g., out1, out2)
    expected_output="${OUTPUT_DIR}out${i:2}"
    # Diff the generated output with the expected output
    diff -w "$expected_output"  "myoutput_$i"
    if [ $? -eq 0 ]; then
        echo "Test case $i passed."
    else
        echo "Test case $i failed."
    fi
    echo "Finished test case: $i"
done

# Cleanup generated output files
rm -f myoutput_*

