number = int (input("Enter a positive integer: "))
result =0
for n in range(1 , number):
    if n % 2 ==0:
        result= result + n
result= result + number
print (result)