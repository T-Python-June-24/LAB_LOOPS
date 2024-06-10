rangOfNumber= range(45, 210)

for num in rangOfNumber:
    if num == 100:
        continue
    if num == 205:
        break
    print(num)


question = "what is the product of 7 * 24 ?"

while int(input(question)) != 168 :
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly3")