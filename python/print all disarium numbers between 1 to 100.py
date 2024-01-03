# Write a Python program to print all disarium numbers between 1 to 100.

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
    # Iterate through numbers from 1 to 100 and check for Disarium numbers
    print("Disarium numbers between 1 and 100:")
    for i in range(1, 101):
        if is_disarium_number(i):
            print(i)