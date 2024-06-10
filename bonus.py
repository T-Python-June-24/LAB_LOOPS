userinput:int = int(input("Enter a Positve number please  "))
userNumber= range(1, userinput+1,1 )
answer:int=0
for x in userNumber:
    if x%2==0:
        answer += x  
print(answer)