# Define a function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        # If the number is divisible by 2, it's even
        print(f"{number} is Even")
    else:
        # Otherwise, it's odd
        print(f"{number} is Odd")

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Call the function with the user-provided number
check_even_odd(num)
