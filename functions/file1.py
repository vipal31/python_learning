# Simple function with no parameters
def say_hello():
    print("Hello, World!")

# Call the function
say_hello()  # Output: Hello, World!

# Function with a single parameter
def greet(name):
    print(f"Hello, {name}!")

# Call the function with an argument
greet("Alice")  # Output: Hello, Alice!

# Function that returns a value
def add_five(number):
    return number + 5

# Call the function and store the result
result = add_five(10)
print(result)  # Output: 15