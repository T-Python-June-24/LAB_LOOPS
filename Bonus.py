while True:
    userInput = int(input("Please Enter Positive Number: "))  
    if userInput % 2 == 0 and userInput > 0 : 
        sumNumbers=0
        for num in range( 1, userInput + 1):
                if num % 2 == 0:
                    sumNumbers += num 
        print(sumNumbers)
            
        break
    else:    
        print("Warning!! This is Odd number, you must Enter Even number")

