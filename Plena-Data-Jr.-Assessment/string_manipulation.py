"""
Problem:
Create an application that will prompt for a user to input a string.
Using the user’s inputted string, find the first letter that is not repeated.
 
For example: If given the string ‘Bubble’, the letter ‘u’ would be the first character returned from the program.
Once the first character is found and displayed back to the user, rewrite the string in order of number of occurrences and order from the inputted string.
In the above example ‘Bubble’ would then be rewritten as ‘uleBbb’. Display this to the user.

"""
from collections import OrderedDict


def get_input():
    """
    Ask user in the prompt for string input
    """
    return input("Please enter your string input here : ")


def string_processing():
    """
    Main program to process the user given input as given rules
    """
    # ask user for the input
    input_str = get_input()
    # handle the test case where user provide empty string
    if not input_str:
        return ""
    # dictionaries to save unique characters
    # and frequency of each characters separately
    unique_char = OrderedDict()
    char_freq = OrderedDict()
    # loop to iterate the given input and stroe in the dictionaries
    for character in input_str:
        # By assumption, characters are not case-sensitive
        character = character.lower()
        if character in char_freq:
            char_freq[character] += 1
        else:
            char_freq[character] = 1

        if character in unique_char:
            # removing duplicate character
            del unique_char[character]
        else:
            unique_char[character] = 1
    # storing unique characters in a list
    char_list = [key for key in unique_char.keys()]
    print("First Unique Character : {}".format(char_list[0]))
    # sorting the character in the increasing order of their frequency
    char_list = [
        key*val for key, val in 
        sorted(char_freq.items(), key=lambda x: x[1])
        ]
    print("Rewritten as : ", end="")
    # returning the rewritten string
    return "".join(char_list)


if __name__ == '__main__':
    print(string_processing())

"""
Note:
For the first category of finding first unique character, 
the example test case is showing that the string is "case-sensitive".
If not case-sensitive, then the first unique letter would be "B" instead of "u".

But for the second category of returing the increasing order of character frequency by the input order, 
the example test case is showing that the string is not "case-sensitive".
If it is case-sesitive, then the expected answer would be "Bulebb".

In such case, I provided my solution by the ASSUMPTION that the given user input is NOT case-sensitive.
"""
