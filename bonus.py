
number = int(input("please enter a positive integer: "))

sum = 0 
i = 2
while i <= number:
    sum += i
    i = i + 2 
   
print(f"The sum of even numbers between 1 and {number} is {sum}")  