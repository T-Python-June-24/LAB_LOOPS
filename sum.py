z = int(input("Insert a positive integer greater than 4: "))
a = 0
sum = 0

while a <= z:
    if a % 2 == 0:
        sum += a
    a += 1
print("The sum of even numbers between 1 and", z , "is" , sum)