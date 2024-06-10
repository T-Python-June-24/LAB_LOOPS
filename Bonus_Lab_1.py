number:int = int(input("enter a positive integer: "))
summation:int = 0
for n in range(1, number + 1):
    if n % 2 == 0:
        summation += n
else:
    print(f"The sum of even numbers between 1 and {number} is {summation}.")