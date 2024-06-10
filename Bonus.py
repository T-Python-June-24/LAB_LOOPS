numbers= int(input("Enter a positive integer : "))
numbers_range=range(1,numbers+1)
sum:int=0
for i in numbers_range :
    if i%2==0:
       sum = sum+i
    else :
        continue
print(f"The sum of even numbers between 1 and {numbers} is {sum} . ")
