"""
Directions: Create a Python module named csp1-4-1a.py.  Add the following code to the module.
Do not forget to test!!!


*** Contact Class ***
1. Define a class named Contact containing the following attributes:
        INITIALIZE ATTRIBUTES with values 0 or empty string ""
    a. Attributes:
        i.      contactID (int)
        ii.     name (String)
        iii.    gender (String)
        iv.     phoneNumber (String)
"""
# Define the Contact class here




"""
* Testing the Contact Class *
	1. Create an instance of Contact.
    2. Set the following values in your new contact object:
        contactID: 101
        name: "Tommy Tutone"
        gender: "Male"
        phoneNumber "867-5309"
    3. Print the attributes of your Contact object using descriptive headings.
"""
# Test the Contact class here
print("*** Testing the Contact Class ***")




"""
*** Dog Class ***
1. Define a class named Dog containing the following attributes:
        INITIALIZE ATTRIBUTES with values 0, empty string "", or False
    a. Attributes:
        i. name (String)
        i. age (int)
        ii. breed (String)
        iii. isNeutered (Default to False)
"""
# Define the Dog class here




"""
* Testing the Dog Class *
	1. Create an instance of Dog.
    2. Set the following values in your new contact object:
        name: "Chilli"
        age: 12
        breed: "Stone County Hill Dog"
        isNeutered = True
    3. Print the attributes of your Contact object using descriptive headings.
"""
# Test the Dog class here
print("*** Testing the Dog Class ***")



"""
*** Creature Class ***
1. Define a class named Creature containing the following attributes:
    a. Attributes:
            INITIALIZE ATTRIBUTES with values 0, empty string "", or False
        i.  type (String)
        ii. size (String)
        iii. speedMPH (int)
        iv. isUgly (boolean - default to False)
    b. Within the Creature class, define a breathe() method that RETURNS the following string:
        i. “The creature breathes”

        WARNING: Make sure you have the self keyword within the paranthesis.
            ALL class methods require the self keyword.
"""
# Define the Creature class here




"""
* Testing the Creature Class *
	1. Create an instance of Creature.
    2. Set the following values in your new Creature object:
        type: = "Hobgoblin"
        size: "220 lbs"
        speedMPH: 26
        isUgly: True
    3. Print the attributes of your Creature object using descriptive headings.
    4. Call the breathe() method and print the value returned using an appropriate heading.
"""
# Test the Creature class here
print("*** Testing the Creature Class ***")




"""
*** Enemy Class ***
1. Define a class named Enemy containing the following attributes:
    a. Attributes:
            INITIALIZE ATTRIBUTES with values 0 or empty string ""
        i. name (String)
        ii. health (int)
    b.  Create a method called decreaseHealth() that takes in a parameter named amount and
        decreases the health by that much. Inside that method, print that the “enemy died” if
        health goes below zero.
"""
# Define the Enemy class here




"""
* Testing the Enemy Class *
	1. Create an instance of Enemy.
    2. Set the following values in your new Enemy object:
        name: = "Maleficient"
        health: 45
    3. Print the attributes of your Enemy object using descriptive headings.
    4. Call the decreaseHealth method passing in the value of 50.
    5. Print the new health of the Enemy.
"""
# Test the Enemy class here
print("*** Testing the Enemy Class ***")




"""
*** Conclusion Questions ***
1. Think of an example from your daily life where you use abstraction. Describe some of the details you
    discard and some of the generality you gain by using the abstraction.

2. What is the difference between procedural abstraction and data abstraction?

3. The GUI was first developed in 1961 by Ivan Sutherland for his Ph.D. at M.I.T. You might
    watch a 1964 video produced by MIT, especially the demo of Sutherland's work starting at 3:20,
    at http://www.youtube.com/watch?v=USyoT_Ha_bA.

    Bill Gates at Microsoft got inspiration for Windows from Apple's Steve Jobs. Steve Jobs at Apple
    got inspiration for Macintosh from Xerox's Alan Kay.  Alan Kay at Xerox got inspiration for Star from
    Trygve Reenskaug. Trygve Reenskaug created the program Autokon with a graphical user interface in 1963
    to design ships. Trygve Reenskaug got inspiration for Autokon from M.I.T.'s Ivan Sutherland.

    All along the way, GUI programming, object-oriented programming, and abstraction have been
    intertwined. Why do you think GUIs, objects, and abstraction have been connected like this in
    the history of computer science?
"""