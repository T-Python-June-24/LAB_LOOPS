n = int(input("Enter a positive integer: "))
i = 0
sum = 0
while i <= n:
    if i % 2 == 0: 
        sum += i
    i += 1
print(f"The sum of even numbers between 1 and {n} is: {sum}")