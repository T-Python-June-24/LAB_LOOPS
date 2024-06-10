positveNum=int(input("please Enter a positve number: "))
evenSum=0
for i in range(1,positveNum+1):
    if i%2==0:
        evenSum+=i
print(f"The sum of even numbers is {evenSum}")