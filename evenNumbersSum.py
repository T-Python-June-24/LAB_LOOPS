sum = 0
n = int(input("Enter a positive integer:"))
number = n
if number > 0:

    for number in range (1,n+1):
        if number % 2 != 0:
            continue
        sum += number
    print(f"The sum of even numbers between 1 and {n} is {sum}.")
else:
    print("Wrong input! Please enter a positve number")
