numbers:list = range(45, 210)
for number in numbers:
    if number == 100:
        continue
    if number == 205:
        break
    print(number)

problem:str = "What is the product of 7 * 24? "
while float(input(problem)) != 7 * 24:
    print("Your Answer is wrong try again...")
else:
    print("You answered this Question correctly")