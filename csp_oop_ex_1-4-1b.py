"""
DEFINITIONS

Attribute:  Each class below, has at least one attribute defined.  They hold
    data for each object created from the class.

The self keyword:  The first parameter of each method created in a Python program
    must be "self".  Self specifies the current instance of the class.

Instance Variable - A variable (attribute) defined within a class constructor method
    defined using the "self." prefix.  Instance variables may have a different value for each object.

Constructor method – A special method called when an object instance is created.
    Constructors accept parameters and typically are used to set instance variables
    with default values.  Constructors are used to do anything that needs to be done
    when an Object is created.

Getters and Setters – Methods that allow instances of other objects to access (getters)
    or store (setters) values of object variables.


Directions: Create a Python module named csp1-4-1b.py.  Add the following code to the module.
Do not forget to test!!!

Warning: Do not use any input() functions in this exercise.

*** Circle Class ***
1. Define a class named Circle containing the following attributes:
        INITIALIZE ATTRIBUTES with values 0 or empty string ""
    a. Attributes:
        i.      radius (int)
    b. Constructor:
        Create a constructor for the Circle class. This constructor needs to receive
        a radius parameter and set the value of the radius attribute (instance variable)
    c. Methods:
        circumference() - Calculates and RETURNS the circumference of the circle:
                Use the formula C = 2ÃƒÂÃ¢â€šÂ¬r
"""
# Define the Circle class here




"""
* Testing the Circle Class *
	1. Create an instance of Circle passing in a radius value of 150.
    2. Call the circumference() method and print the value returned formatted like:
        The circumference of a circle with a radius of: valuefromradiusattribute = valuereturnedfrommethod.
"""
# Test the Circle class here
print("*** Testing the Circle Class ***")






"""
*** Person Class ***
1. Define a class named Person containing the following attributes:
        INITIALIZE ATTRIBUTES with values 0 or empty string ""
    a. Attributes:
        i. age (int)
        ii. weight (float)
        iii. gender (String)
    b. Constructor:
        Code the constructor to accept parameter values for the three attributes (age, weight, gender).
        Set the properties based upon the parameters passed into the constructor method.
    c. Methods:
        - getAge() and setAge() - used retrieve and modify the age attribute.
        - getWeight() and setWeight() - used retrieve and modify the weight attribute.
        - getGender() and setGender() - used retrieve and modify the gender attribute.

        NOTE: The six methods above are called accessors (getters) and mutators (setters).
"""
# Define the Person class here




"""
* Testing the Person Class *
	1. Create an instance of Person passing in the following values:
        - age: 17
        - weight: 120
        - gender: "Female"
    2. Print the attributes of your Person object using the accessor (getter) methods.
        Be sure to include descriptive headings.
    3. Modify the attribute values using the mutator (setter) methods.  Set the values to:
        - age: 54
        - weight: 220
        - gender: "Male"
    4. Again, print the attributes of your Person object using the accessor (getter) methods.
        Be sure to include descriptive headings.

"""
# Test the Person class here
print("*** Testing the Person Class ***")


