# sample.py

def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

def main():
    user_name = "Alice"
    print(greet(user_name))

    num1 = 5
    num2 = 3
    print(f"{num1} + {num2} = {add(num1, num2)}")

if __name__ ==
