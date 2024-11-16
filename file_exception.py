def divide_numbers():
    while True:
        try:
            # Get input from the user
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))
            
            # Perform the division
            result = numerator / denominator            
            # Display the result
            print(f"The result of {numerator} divided by {denominator} is: {result:.2f}")
            break  # Exit the loop after a successful operation
        except ZeroDivisionError:
            print("Error: Cannot divide by zero. Please enter a non-zero denominator.")
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
def main():
    print("Welcome to the Division Program!")
    divide_numbers()
    print("Thank you for using the program!")
if __name__ == "__main__":
    main()
