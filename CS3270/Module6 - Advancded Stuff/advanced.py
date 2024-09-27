# Advanced tips and tricks in Python
import shutil

def print_centered_with_asterisks(text):
    # Get the terminal width
    terminal_width = shutil.get_terminal_size().columns

    # Calculate the total number of asterisks needed
    text_length = len(text) + 2  # +2 for the spaces around the text
    total_asterisks = terminal_width - text_length

    # Ensure there are at least some asterisks on both sides
    if total_asterisks > 0:
        asterisks_on_each_side = total_asterisks // 2
        left_side = '*' * asterisks_on_each_side
        right_side = '*' * (total_asterisks - asterisks_on_each_side)
        result = f"{left_side} {text} {right_side}"
    else:
        # If the text is too long, just print it as-is
        result = text
    print()
    print(result)
    print()


terminal_width = shutil.get_terminal_size().columns
"""
The use of functions have been a key in modularity and resuability in programming languages. That being said, with new advances in programming languages, the roles of functions have been increased to:
    - simple short and concise code without using complex iteartors or conditional statements.

In this section, we will talk about counter, zip, and itertools functions.

Counter
    Counter is a type of conatianer that keeps track of the count of each element that is present in a container. This can be useful for finding teh data frequency.
"""
print_centered_with_asterisks("Using the Counter Container")

# To show a counter in action:
from collections import Counter

# Apply the counter on a string object
print(Counter("people"))
big_ass_word = "supercalifragilisticexpialidocious"
print(Counter(big_ass_word))

# Apply the counter on a list of objects
list_counter = Counter([1, 2, 1, 2, 3, 4, 1, 3, 1, 1, 1])
print(list_counter.most_common(1))
print(list(list_counter.elements()))

# Appply to a dictionary
print(Counter({'A': 2, 'B': 2, 'C': 2, 'C': 3}))
print(Counter({'A': 2, 'B': 2, 'C': 2, 'C': 3}))
"""
Counter({'p': 2, 'e': 2, 'o': 1, 'l': 1})
Counter({'i': 7, 's': 3, 'c': 3, 'a': 3, 'l': 3, 'u': 2, 'p': 2, 'e': 2, 'r': 2, 'o': 2, 'f': 1, 'g': 1, 't': 1, 'x': 1, 'd': 1})
[(1, 6)]
[1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4]
Counter({'C': 3, 'A': 2, 'B': 2})
"""

"""
Zip
    This zip function is used to create an aggregated iterator based on two or more individual iterators. The zip func is useful when we need to iterate on multiple iterations in parallel.
    Example, we can use zup when implementing mathematical algos that involve interpolation or pattern recognition. This is hellpful in digital processing where we comine mutiple data sources (signals) into a single singnal.
"""
print_centered_with_asterisks("Using ZIP")

num_list = [1, 2, 3, 4, 5]
lett_list = ['alpha', 'bravo', 'charlie']

zipped_iterator = zip(num_list, lett_list)
print(next(zipped_iterator))
print(next(zipped_iterator))
print(list(zipped_iterator))
