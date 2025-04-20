def calculate_digit_sum(number):
    # Convert the number to a string
    num_str = str(number)
    # Initialize a variable to store the sum
    digit_sum = 0
    # Iterate over each character in the string
    for digit in num_str:
        # Convert the character back to an integer and add it to the sum
        digit_sum += int(digit)
        # Return the sum of the digits
    return digit_sum
# Test the function
input_number = int(input("Enter a number: "))
sum_of_digits = calculate_digit_sum(input_number)
print("Sum of digits:", sum_of_digits)
