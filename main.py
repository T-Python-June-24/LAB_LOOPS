
# range from 45 to 210
rng = range(45,210)

print("Solution of the first problem: ")

for num in rng:
    if num == 100:
        continue
    elif num == 205:
        break
    else:
        # print(num)
        pass # just to make the terminal clean

print("-"*20)

print("Solution of the second problem: ")

# hint: answer is 168

while True:
    user_answer = int(input("What is the product of 7 * 24? "))
    if user_answer is not 168:
        print("Your answer is wrong try again ...")
    else:
        print("You answered this question correctly! congrats")
        break
    
print("-"*20)

#  -------
print("Solution of bonus problem: ")

while True:
    user_range = int(input("Enter a positive integer: "))
    
    range_for_calculation = range(1 ,user_range + 1)
    answer = 0
    for number in range_for_calculation:
        if number % 2 == 0:
            print(number)
            answer += number
    print(f"The sum of even numbers between 1 and {user_range} is {answer}")
    break
        


        