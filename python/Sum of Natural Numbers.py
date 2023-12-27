#Write a Python Program to Find the Sum of Natural Numbers.

if __name__ == '__main__':
    limit = int(input("Enter the limit: "))
    # Initialize the sum
    sum=0
    
    # Use a for loop to calculate the sum of natural numbers
    for i in range(1,limit+1):
        print(i)
        sum+=i
    # Print the sum
    print("The sum of natural numbers up to",limit,"is:",sum)
