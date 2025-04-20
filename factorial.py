# Take input from the user
num = int(input("Enter a number: "))

# Initialize factorial to 1 (since factorial of 0 and 1 is 1)
fact = 1

# Loop from 1 to the given number
for i in range(1, num + 1):
    fact *= i  # Multiply current value of fact by i

# Display the result
print(f"Factorial of {num} is {fact}")
