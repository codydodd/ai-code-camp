#print("hello world")

# n = "hello world"
# print(n)

# # String Variable (a string is a series of characters, not numbers)
#name = "Cody"

# # Numeric variable (has no quotations)
#age = 38


# how to print Variables inside a string
#print(f"My name is {name} and may age is {age}")


# # One way to comment is with #


# # Functions are defined by a "def"  and a name and a () for feeding data, and INDENTS
# def function_for_greeting(name):
#     print("I am printing AFTER lines 27") # Bonus, why does this print appears after line 27? 
#     print(f"Hello, {name}!")
# print(f"Hello2, {name}!")



#print("I am printing BEFORE lines 27")
# Call the function
#function_for_greeting("Alice")  # Output: Hello, Alice!
#greet("Bob")    # Output: Hello, Bob! 

# Open the text file for reading
with open('words.txt', 'r') as file:
    content = file.read()  # Read the entire file into a variable
    # Print the content (or process it as needed)
    print(content)
