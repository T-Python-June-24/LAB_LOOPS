
numbers =range(45,210) 
for i in numbers:
   if i== 100 :
      continue
   if i==205:
      break
   print(i)



Question="what's the product of 7 * 24 ? "
while int(input(Question))!= 168 :  #7 * 24=168
   print("Your Answer is wrong try again..")
else :
   print("You answered this Question correctly")
