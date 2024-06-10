y = float(input("What is the product of 7 by 24?: 7 * 24 = "))

while y != 168:
    print("Your answer is wrong")
    y = float(input("Please Try Again: 7 * 24 = "))
else:
    print("You got it right, it's 168")