# Write a program that reads a stream of numbers from one file and writes the
# numbers in sorted (ascending) order to a second file.  Specifically, your
# program must ask the user to enter the name of the input file and the name of
# the output file.  Then, read every number (each on their own line) from the
# input file, sort them, and print them (each on their own line) to the output
# file.
#
# You are required to create at least 1 function to solve this problem:
#
# 1) A function named sort_data(), that takes two parameters.  The first
#    parameter is an already opened file handle on the input file.  The second
#    is an already opened file handle on the output file.  The function must
#    handle the reading, sorting, and writing of the data.
#
# Your input and output messages must conform to the following examples.  Note
# that in the first example, the file "not_there.txt" does not exist.  In the
# second example, "some_data.txt" exists and contains all numbers.  After the
# program ends, the file "sorted_data.txt" has the same data as "some_data.txt"
# but in ascending order.  You will have to create your own files for testing
# purposes.
#
# Enter the input file name: not_there.txt
# Enter the output file name: something.txt
# File Error!
#
# Enter the input file name: some_data.txt
# Enter the output file name: sorted_data.txt
#
# Note the order of inputs, capitalization of messages, spacing, etc. 


import sys

def sort_data(opened_input_file, opened_output_file):
    sorted_numbers = []
    for number in opened_input_file:
        sorted_numbers.append(float(number))
    sorted_numbers.sort()
    for number in sorted_numbers:
        print(number, file=opened_output_file)
        

input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")
try:
    with (
        open(input_file) as in_file,
        open(output_file, "w") as out_file
        ):
        sort_data(in_file, out_file)

except IOError:
    print("File Error!")
    sys.exit()

