rangeOfNumbers=range(45,211)
for num in rangeOfNumbers:
    if num ==100:
        continue
    elif num  ==205:
        break
    print(num)
while True:
    answer=int(input("What is the product of 7*24 ? : "))
    if (answer==7*24):
        print("You answered this Question correctly")
        break
    print("Your Answer is wrong try again..")
