'''
while True :
    try:  
        numbers= int(input("Enter a positive integer : "))
        print("integer ")
        break
    except ValueError:
        print("invalid input, please enter a number")
'''
numbers= int(input("Enter a positive integer : "))
while numbers<0 :
    numbers =int (input("invalid input, please enter a positive number : "))
else :
      numbers_range=range(1,numbers+1)
      sum:int=0
      for i in numbers_range :
         if i%2==0:
           sum = sum+i
         else :
          continue
print(f"The sum of even numbers between 1 and {numbers} is {sum} . ")
