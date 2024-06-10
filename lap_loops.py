for num in range(45, 211):
    if num == 100:
        continue
    if num == 205:
        break
    print(num)


answer = "what is the product of 7 * 24 ?"

while input(answer) != "168":
    print("Your Answer is wrong try again..")
else:
   print("You answered this Question correctly")