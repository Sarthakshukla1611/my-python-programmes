def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

try:
    number = int(input("Enter a number to find its factorial: "))
    print(f"Factorial of {number} is {factorial(number)}")
except ValueError:
    print("Please enter a valid integer.")
