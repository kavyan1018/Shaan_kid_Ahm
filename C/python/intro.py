# comments -> Single line

'''
    this is a multi line comments  -->  ("""  """) (''' ''')
'''


# c -> printf -> py -> print
# c -> header files -> in py we dont need header file 
# printf();   -> ; in not accepted here  
# ("%d", a) in c ->  in py () -> %d in not accepeted only direct varibales 



# a = 100
# print(a)

# user input

# c -> scanf -> py -> input()

# a = input("Enter a number: ")  # always takes input
# print(a)


# type casting
# a = int(input("Enter a number: ")) 
# print(a)


# a = float(input("Enter a number: "))
# print(a)

# a = str(input("Enter a string: "))
# print(a)


# if - else 

'''
    syntax of if else :
        c : 
            if(condition)
            {
                // statements
            }
            else
            {
                // statements   
            }
    
        py :
            if condition :
                # statements
            else :
                # statements
    
'''
"""
a = int(input("Enter a number: "))
if a % 2 == 0 :
    print("Even Number")
else :
    print("Odd Number")
"""
    
    
# a = int(input("Enter a age to check your eligible for Vote or not : "))

# if a >= 18:
#     print("You are eligible for Vote")
# else :
#     print("You are not eligible for Vote")



'''
else if :
    c :
        if(condition1)
        {
            // statements
        }
        else if(condition2)
        {
            // statements
        }
        else
        {
            // statements
        }
        
        
    py :
        if condition1 :
            # statements
        elif condition2 :
            # statements
        else :
            # statements

'''


# Write a program in python to check if the given number is positive, negative or zero.


num = float(input("Enter a number: "))
if num > 0 :
    print("Positive Number")
elif num == 0 :
    print("Zero")
else :
    print("Negative Number")