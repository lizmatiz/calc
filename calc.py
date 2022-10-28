#Elizabeth Hooton
#eh151720@ohio.edu
#Section 100
import math
print (""" 
                                      88           
                                ,d    88           
                                88    88           
88,dPYba,,adPYba,  ,adPPYYba, MM88MMM 88,dPPYba,   
88P'   "88"    "8a ""     `Y8   88    88P'    "8a  
88      88      88 ,adPPPPP88   88    88       88  
88      88      88 88,    ,88   88,   88       88  
88      88      88 `"8bbdP"Y8   "Y888 88       88  
                                                   
""") # cute math title                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
menu = """
Enter number of operation that you want to execute <type exit or quit to end program>:
1: sin(x)
2: cos(x)
3: tan(x)
4: asin(x)
5: acos(x)
6: atan(x)
7: ln(x)
8: sqrt(x)
9: factorial(x)
"""
print(menu)
user_choice = input("Enter your choice(1-9):\n")

inputs = [] # creates a list of inputs

while user_choice.lower() not in ["exit", "quit"]:

    
    if user_choice == "1": # if the user choice is 1, then...
        user_num = float(input("\nEnter a value for x:\n")) # the user_num input is a float, prompts with "Enter a value of x:
        math_sin = math.sin (user_num) # sets math_sin to the sin of user_num
        print ('\nsin(',user_num,') =', math_sin) # prints the number
        inputs.append ('Func: ' + str(user_choice) + ' | Arg: ' + str(user_num)) # creating a list for history
         
    elif user_choice == "2": # if the user choice is not 1, and the user choice is 2, then...
        user_num = float(input("\nEnter a value for x:\n")) # the user_num input is a float, prompts with "Enter a value of x:
        math_cos = math.cos (user_num) # sets math_cos to the cosine of user_num
        print ('\ncos(',user_num,') =', math_cos) # prints the number
        inputs.append ('Func: ' + str(user_choice) + ' | Arg: ' + str(user_num)) # creating a list for history

    elif user_choice == "3": # if the user choice is not 1 or 2, and the user choice is 3, then...
        user_num = float(input("\nEnter a value for x:\n")) # the user_num input is a float, prompts with "Enter a value of x:
        math_tan = math.tan (user_num) # sets math_tan to the tan of user_num
        print ('\ntan(',user_num,') =', math_tan) # prints the number
        inputs.append ('Func: ' + str(user_choice) + ' | Arg: ' + str(user_num)) # creating a list for history

    elif user_choice == "4": # if the user choice is not 1, 2, or 3, and the user choice is 4, then...
        user_num = float(input("\nEnter a value for x:\n")) # the user_num input is a float, prompts with "Enter a value of x:
        if user_num >=-1 and user_num<=1:
            math_asin = math.asin (user_num)# sets math_asin to the asin of user_num
            print ('\nasin(',user_num,') =', math_asin) # prints the number
            inputs.append ('Func: ' + str(user_choice) + ' | Arg: ' + str(user_num)) # creating a list for history
        else:
            print (' ')
            print (user_num, 'is not within the domain of asin()')
            
    elif user_choice == "5": # if the user choice is not 1, 2, 3, or 4, and the user choice is 5, then...
        user_num = float(input("\nEnter a value for x:\n")) # the user_num input is a float, prompts with "Enter a value of x:
        if user_num >=-1 and user_num<=1:
            math_acos = math.acos (user_num) # sets math_acos to the acos of user_num
            print ('\nacos(',user_num,') =', math_acos) # prints the number
            inputs.append ('Func: ' + str(user_choice) + ' | Arg: ' + str(user_num)) # creating a list for history
        else:
            print (' ')
            print (user_num, 'is not within the domain of acos()')

    elif user_choice == "6": # if the user choice is not 1, 2, 3, 4, or 5, and the user choice is 6, then...
        user_num = float(input("\nEnter a value for x:\n")) # the user_num input is a float, prompts with "Enter a value of x:
        math_atan = math.atan (user_num) # sets math_atan to the atan of user_num
        print ('\natan(',user_num,') =', math_atan) # prints the number
        inputs.append ('Func: ' + str(user_choice) + ' | Arg: ' + str(user_num)) # creating a list for history

    elif user_choice == "7": # if the user choice is not 1, 2, 3, 4, 5, or 6, and the user choice is 7, then...
        user_num = float(input("\nEnter a value for x:\n")) # the user_num input is a float, prompts with "Enter a value of x:
        if user_num >0:
            math_log = math.log (user_num)
            print ('\nln(',user_num,') =', math_log) # prints the number
            inputs.append ('Func: ' + str(user_choice) + ' | Arg: ' + str(user_num)) # creating a list for history
        else:
            print (' ') # adds a line
            print (user_num, 'is not within the domain of ln()') # lets the user know that the number they entered is not within the domain
            
    elif user_choice == "8": # if the user choice is not 1, 2, 3, 4, 5, 6, or 7, and the user choice is 8, then...
        user_num = float(input("\nEnter a value for x:\n")) # the user_num input is a float, prompts with "Enter a value of x:
        if user_num >=0:
            math_sqrt = math.sqrt (user_num) # sets math_sqrt to the sqrt of user_num
            print ('\nsqrt(',user_num,') =', math_sqrt) # prints the number
            inputs.append ('Func: ' + str(user_choice) + ' | Arg: ' + str(user_num)) # creating a list for history
        else:
            print (' ') # adds a line
            print (user_num, 'is not within the domain of sqrt()') # lets the user know that the number they entered is not within the domain
            
            
    elif user_choice == "9": # if the user choice is not 1, 2, 3, 4, 5, 6, 7, or 8, and the user choice is 9, then ...
        user_num = float(input("\nEnter a value for x:\n")) # the user_num input is a float, prompts with "Enter a value of x:
        if user_num >=0:
            if int(user_num) == user_num: # makes sure that the float number of user_num is equal to the integer version
                math_factorial = math.factorial (int(user_num)) # converts math_factorial to an integer
                print ('\nfactorial(',user_num,') =', math_factorial) # prints the number
                inputs.append ('Func: ' + str(user_choice) + ' | Arg: ' + str(user_num)) # creating a list for history
            else:
                print (' ') # adds a line
                print (user_num, 'is not an integer') # if the float is not equal to the integer, then it prints a statement
        else:
            print (' ') # adds a line
            print (user_num, 'is not within the domain of factorial()') # lets the user know that the number they entered is not within the domain

    else:
        print ('') # adds a line
        print (user_choice, 'is not a valid option') # if the user choice is not 1, 2, 3, 4, 5, 6, 7, 8, or 9, then it prints a statement 
        
    print(menu)
    user_choice = input("Enter your choice(1-9):\n") # restarts the process
    
print ('\nList of the functions & arguments <3: \n') # prints the title of the list

for input in inputs:
    print(input + '\n') # prints the list
    
  
print ('''

           __
      (___()'`;
      /,    /`
      \\"--\\


     ''') # this is the dog who helps with math (:

    

    
    

print("=== Program complete ==")
