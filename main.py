# String Practice:

# Create a Python program that asks the user to input a sentence.
p=print
s=input("Type a sentence about your favorite movie:")
# Print the first and last letter of the sentence.
p(s[0:1]),p(s[-1:])
# Convert the entire sentence to uppercase and print the result.
p(s.upper())
# Find and print a substring from the inputted sentence.
p(s[0:3])
# Replace a word in the sentence and print the updated sentence.
p(s.replace("its","it isnt"))
# Input Practice:

# Create a Python program that asks the user for their name, age, and favorite movie.
name=input("What is your name?")
age=int(input("How old are you?"))
movie=input("What is your favorite movie?")

# Print a message back to the user with this information.
print(f"Your name is {name}, your age is {age}, and your favorite movie is {movie} ")
# Note: Make sure to convert the age to an integer.


# F-String Practice:

# Create a Python program that asks the user for three objects in the room.
thing_1=input("Type one thing you see around the room:")
thing_2=input("Type another thing you see around the room:")
thing_3=input("Type one more thing you see around the room:")
# Create variables from these objects and insert those variables into an f-string sentence.
# Print the f-string sentence.
print(f"Three objects you see around the room are {thing_1}, {thing_2}, and {thing_3}. ")
# Advanced String Practice:

# Create a Python program that reverses the words in a sentence inputted by the user.
anything=input("Type a sentence about anything:")

sentence = "dread it run from it destiny still arrives"
word_list = sentence.split()
reversed_list = word_list[:: -1]
reversed_sentence = " ".join(reversed_list)
print(reversed_sentence)
# For example, if the user inputs "Python is fun", the program should print "fun is Python".
# Advanced Input Practice:

# Create a Python program that asks the user for the name of their favorite book, movie, and song.

# Print a message that says, "Your favorite book is [Book], your favorite movie is [Movie], and your favorite song is [Song]."


# Advanced F-String Practice:

# Create a Python program that asks the user for their name, age, and the current year.
# Use f-strings to print a message like: "Hello [Your Name], you were born in [Current Year - Your Age]."

# Type Conversion Practice:

# Create a Python program that asks the user for two numbers.
# Print the sum, difference, product, and quotient of the two numbers.
# Note: Make sure to convert the input to integers before performing any calculations.

# Summary Challenge:

# Find a summary of a movie online and create a variable called movie_summary and store the summary in this variable.
# Print the length of the summary.
# Uppercase the entire summary and print it.
# Replace a word in the summary and print the updated summary.
# Print the last word of the summary.


# Real Challenge:

# Create a Python program that asks the user for their first and last name, their age, and their favorite color.
# Using f-strings, print a message that says, "Hello [First Name] [Last Name], you are [Age] years old and your favorite color is [Favorite Color]."