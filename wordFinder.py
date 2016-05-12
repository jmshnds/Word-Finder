# Description: A program that checks if each permutation
# of a word(s) is in a specified text file and prints out
# the words that were found in the file.
# 
# Date: 12 May 2016

from itertools import permutations
import re

scrambledWords = []
for i in range(0, 5): # prompt the user for 5 strings
    scrambledWords.append(input("Enter word " + str(i+1) + ": "))

unscrambledWords = []

fileName = input("Enter the name of the file you wish to open: ");
for word in scrambledWords:
    perm = [''.join(p) for p in permutations(word)]
    perm = set(perm)    # convert perm to a set object(only unique entries)

    with open(fileName, 'r') as fin:
        for line in fin:  # for each line in f, check if it is a member of the perm set
            line = re.sub('[\n ]', '', line)    # remove any extra whitespace from line(new line and space)
            if line in perm:
                unscrambledWords.append(line)
    fin.close()

print("The words that were found are: ")
for w in unscrambledWords:  # print the result separated by commas
    print(w + ',', end="")

