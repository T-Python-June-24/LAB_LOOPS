i= 1
while i<=3:
    question= int(input("what is the product 7 * 24 ? "))
    if question == 168:
        print("you answered this question correctly")
        break
    else:
        i+=1
        print("your answer is wrong try again..")
else: 
    print("Exceeded number of attempts ")
    
