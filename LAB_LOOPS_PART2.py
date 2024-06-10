'''
Using a while loop and input , do the following :

Ask the the user : "what is the product of 7 * 24 ?"
check if the answer is right then exit the loop and print "You answered this Question correctly"
if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again

'''
correct_answer = 7 * 24  

while True:

    user_answer:int = int(input("what is the product of 7 * 24 ?")) 

    if user_answer != correct_answer:

        print("Your Answer is wrong try again.." )
    
    else:
       
        print("You answered this Question correctly")
        
        break
