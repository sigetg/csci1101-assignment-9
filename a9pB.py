# Write a program to analyze word usage in a file.  Specifically, write a
# program that prompts the user for a filename, opens that file, and counts how
# many times each word appears in the file.  The program will print out two sets
# of words at the end.  First, it will print all the words that appear the most
# frequently.  Second, it will print all the words that appear exactly once.
#
# Note that, unlike previous problems, each line might contain many words on it.
# Words should be treated in a case insensitive manner.  Your program will also
# need to remove all punctuation at the beginning and ending of each word so
# that they will be counted correctly.  You will use two new (but simple)
# functions to help with this.  First, string.split() will take a string (e.g.,
# a line from a file), split that string into words (based on whitespace), and
# return those words in a list.  Second, we've used string.strip() many times
# already to remove leading and trailing whitespaces from a string.  strip()
# also takes an optional parameter which is a string of characters to be removed
#  from the beginning and end.  For example:
#
# s = "-something!"
# s = s.strip("!-")
# # s is now equal to "something" with all leading/trailing ! and - removed
#
# You can use this to remove all punctuation from a word.  Even better, as this
# is a common thing to do, Python provides a constant string you can use that
# already includes every possible punctuation character: string.punctuation.
# You have to import string to use it.  For example:
#
# import string
#
# s = "-.something!."
# s = s.strip(string.punctuation)
# # s is now equal to "something" with all leading/trailing punctuation removed
#
# You are required to create at least 3 functions to solve this problem:
#
# 1) A function named get_word_counts(), that takes a single parameter, an
#    already opened file handle on the file to read.  The function returns a
#    dictionary that contains every word (with punctuation removed) from the
#    file and how many times that word appeared.  Again, note that each line in
#    the file might have multiple words on it.
# 2) A function named get_most_common_words(), that takes a dictionary of word
#    counts as a parameter.  The function returns two values: the maximum word
#    count, and a list of all words that appear that maximum number of times.
# 3) A function named get_once_words(), that takes a dictionary of word counts
#    as a parameter.  The function returns a list of all words that appear
#    exactly once.
#
# Your input and output messages must conform to the following examples.  Note
# that in the first example, the file "nope.txt" does not exist.  In the second
# example, "jedi_code.txt" exists with the following contents:
#
# There is no emotion, there is peace.
# There is no ignorance, there is knowledge.
# There is no passion, there is serenity.
# There is no chaos, there is harmony.
# There is no death, there is the Force.
#
# You will have to create your own files for testing purposes.
#
# Enter the input file name: nope.txt
# Error with jedi_code.tzt!
#
# Enter the input file name: jedi_code.txt
# Most common words (10 times): there is
# Words appearing once: emotion peace ignorance knowledge passion serenity chaos
# harmony death the force
#
# Note the order of inputs, capitalization of messages, spacing, etc.

import string
import sys

def get_word_counts(opened_input_file):
    word_counts = {}
    for line in opened_input_file:
        line = line.strip(string.punctuation)
        word_list = line.split()
        for word in word_list:
            word = word.strip(string.punctuation)
            word = word.lower()
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
    return word_counts

def get_most_common_words(my_dict):
    max_times = 0
    max_words = []
    for key in my_dict:
        if my_dict[key] >= max_times:
            max_times = my_dict[key]
            max_words.append(key)
    return max_times, max_words

def get_once_words(my_dict):
    once_words = []
    for key in my_dict:
        if my_dict[key] == 1:
            once_words.append(key)
    return once_words
        

input_file = input("Enter the input file name: ")

try:
    with open(input_file) as in_file:
        x = get_word_counts(in_file)
        max_times, max_words = get_most_common_words(x)
        once_words = get_once_words(x)
        print(f"Most common words ({max_times} times): ", end="")
        for word in max_words:
            print(word, end=" ")
        print("\n", end="")
        print("Words appearing once: ", end="")
        for word in once_words:
            print(word, end=" ")

except IOError:
    print("File Error!")
    sys.exit()









