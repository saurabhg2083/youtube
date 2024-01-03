# Write a Python program to check if the given number is a Disarium Number.
# A Disarium number is a number that is equal to the sum of its digits each raised to thepower of its respective position.

def is_disarium_number(num):
    # Convert the number to a string to iterate through its digits
    num_str = str(num)
    length = len(num_str)
    sum_of_digits = 0

    # Calculate the sum of digits powered with their respective positions
    for i in range(length):
        sum_of_digits += int(num_str[i]) ** (i + 1)

    # Check if the sum of powered digits is equal to the original number
    return sum_of_digits == num


if __name__ == '__main__':
    # Input a number to check for Disarium property
    number = int(input("Enter a number to check if it's a Disarium number: "))

    # Check if the number is a Disarium number and display the result
    if is_disarium_number(number):
        print(f"{number} is a Disarium number")
    else:
        print(f"{number} is not a Disarium number")