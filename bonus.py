sum = 0
message = "Enter a positive integer number:"
while True : # for check that the number is positive 
    user_input = int(input(message))
    if user_input < 0 :
           
           message = "plase enter positive integer! : "

    else:
        break

for number in range(1,user_input+1):
            if number % 2 == 0 :
                sum += number
  
print(f"the sum of even numbers between 1 and {user_input} is {sum}")


