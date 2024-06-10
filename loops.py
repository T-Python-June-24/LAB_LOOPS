numbers = range(45, 210)
for i in numbers :
    if i == 100:
        continue
    if i == 205:
        break
    print(i)



question = "What is the product of 7 * 24? "
while input(question) != "168":
    print("Your answer is wrong, try again.")
    print(input(question))
else:
    print("You answered this question correctly.")
