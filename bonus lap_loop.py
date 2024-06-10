n = 0
sum ="Enter a positive integer:"
while True : 
    user=int(input(sum))
    if user<0:
        sum="plase enter positive integer:"
    else:
        break
    for number in range(1,user+1):
      if number %2==0:
          n+=number
          print(f"sum even number between 1 and {user}is {sum}")
'''
Write a Python program that prompts the user for a positive integer `n`, and then calculates the sum of all even numbers between 1 and `n`, inclusive.

Your program should use a loop (either a `for` loop or a `while` loop) to iterate over the numbers between 1 and `n`, 
and only add the even numbers to the sum.

For example:
Enter a positive integer: 10
The sum of even numbers between 1 and 10 is 30.
In this example, the even numbers between 1 and 10 are 2, 4, 6, 8, and 10, and their sum is 30.
'''