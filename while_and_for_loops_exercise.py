'''
python Basics
======================

Directions
----------
Create a module on your z:\ drive named z:\csp\while_and_for_loops_exercise.py.  Copy 
    this text and paste it into the newly created file.

** Problem 1 (printNumbers() function)**

1) Create a function named printNumbers() It should accept parameters named 
    startNumber and endNumber and print two lists between (and including) them.
2) Using a while loop, print a list of numbers between startNumber and 
    endNumber (inclusive).
3) Using a for loop, print a list of numbers between startNumber and 
    endNumber (inclusive).  You must use the range() function in the for loop.
        Hint: Read about the range() function.  You will be using advanced
            range() features in several parts of this exercise.
4) Call the printNumbers() function passing in a value for startNumber and endNumber.
    Note: There is no value returned from this function.
5) Test multiple times.

Write your code below:
'''





'''
** Problem 2 (Data Entry Loop)**

1) Create a function named myFamily(). It should accept no parameters.
2) Inside the myFamily() function, use the input() function, inside a
    while loop, to allow the user to enter family members.  They should 
    press x after all family members have been entered.
        Example Message:
            "Please enter the name of a family member.  Enter x when finished".
  b) Print each member after they are entered.
  c) Exit the loop when the user enters "x" or "X".
        Note: Do not use the or operator.  Instead use the .lower() method to
        convert the value entered to lower case inside the if statement.
        Note2: Print the value entered only if it is valid (not "X" and not "").
                Consider using the .strip() function to remove spaces from entered value.
3) Print the message "Family entered" after the loop has completed.
4) Test the myFamily() function several times until you are satisfied it works correctly.


Write your code below:
'''



'''
** Problem 3 (printNested() function)**

1) Create a function named printNested(). It should accept one parameter named endValue.
    It will print from zero to the the value of the endValue parameter two times.
    OUTPUT:
    If printGrid were called using the value 3 as the parameter, the output woud be:
                    >>> 
                    Outside loop: 0  Inside Loop: 0
                    Outside loop: 0  Inside Loop: 1
                    Outside loop: 0  Inside Loop: 2
                    Outside loop: 1  Inside Loop: 0
                    Outside loop: 1  Inside Loop: 1
                    Outside loop: 1  Inside Loop: 2
                    Outside loop: 2  Inside Loop: 0
                    Outside loop: 2  Inside Loop: 1
                    Outside loop: 2  Inside Loop: 2
                    >>> 
2) Use a nested while loop to print the output.
3) Do the same as the following step using a nested for loop.
4) Call the printNested() function and check the output carefully.


Write your code below:
'''



'''
** Problem 4 (asciiArt() function)**

1) Create a function named asciiArt(). It should accept one parameter named size.
    Code eight loops (four while and four for loops)
    OUTPUT:
    If asciiArt() were called using the value 5 as the parameter, the output woud be:
                         ** WHILE LOOPS ** 


                         *** The Mario platform ***

                            #
                           ##
                          ###
                         ####
                        #####

                         *** The upside down Mario platform ***
                        #####
                         ####
                          ###
                           ##
                            #

                         *** The reverse of Mario platform ***
                        #
                        ##
                        ###
                        ####
                        #####
                        
                          *** The upside down reverse of Mario platform ***
                        #####
                        ####
                        ###
                        ##
                        #
                         ** FOR LOOPS ** 


                         *** The Mario platform ***

                            #
                           ##
                          ###
                         ####
                        #####

                         *** The upside down Mario platform ***
                        #####
                         ####
                          ###
                           ##
                            #

                         *** The reverse of the Mario platform ***
                        #
                        ##
                        ###
                        ####
                        #####

                         *** The upside down reverse of Mario platform ***
                        #####
                        ####
                        ###
                        ##
                        #
2) Print the first four using while loops.
3) Print the second four using for loops.
4) Call the asciiArt() function several times using different values for size.
5) Check output thoroughly.


Write your code below:
'''


