"""
Directions: Create a Python module named csp1-4-1c.py.  Add the following code to the module.
Do not forget to test!!!

Warning: Do not use any input() functions in this exercise.

!!!!!!  NEW TERMS  !!!!!!
Inheritance: When a class copies all methods and properties from another class.

Superclass - The class from whom the methods and properties are being copied.  It is
    also called the parent or base class.

Subclass - The class that is copying (inheriting) the methods and properties
    from the Superclass.  It is also called the child class.

Inheritance Example: In the class diagram below, Feline and Canine are subclasses
of the Mammal class. Mammal is a subclass of Animal. When we create an instance of the 
Mammal class, all methods and properties from Animal class are included.

In this exercise, you will create an Animal class which will be the superclass for Mammal.
                You will then create the Feline and Canine classes which are subclasses of Mammal.

*** 1-4-1c Basic Class Diagram ***
                     ___________
                    |  Animal   |
                    |-----------|
                    |  gender   |
                    |getGender()|
                    |setGender()|     |
                    |           |
                     ----------
                          /\
                         //\\
                          ||
                     _____||___
                    |  Mammal  |
                    |----------|
                    |   age    |
                    | getAge() |
                    | setAge() |
                     ----------
                           /\
                          //\\
          ___________      ||     ____________
         |  Feline   |     ||    |  Canine    |
         |-----------|           |------------|
         | isIndoor  |-----------|height      |
         |getIndoor()|           |getHeight() |
         |setIndoor()|           |setHeight() |
         |           |           |            |
          ----------              ------------



*** Animal Class ***
1. Define a class named Animal containing the following attributes:
        INITIALIZE ATTRIBUTES with values empty string ""
    a. Attributes:
        gender (String)
    b. Constructor:
        Create a constructor for the Animal class. This constructor needs to receive
        the value for gender and save it as an instance variable.
    c. Methods:
        getGender() - returns the value of the gender instance variable (accessor method)
        setGender() - sets the value of the gender instance variable (mutator method)

     Example accessor and mutator methods for an attribute named color:
     -----------------------------------
				def setColor(self, color):
					self.color = color

				def getColor(self):
					return self.color
"""
# Define the Animal class here




"""
* Testing the Animal Class *
	1. Create an instance of Animal passing in a gender value of "Female".
    2. Print the attributes of your Animal object using the accessor (getter) methods.
        Be sure to include descriptive headings.
    3. Modify the attribute values using the mutator (setter) methods.  Set the values to:
        - gender: "Male"
    4. Again, print the attributes of your Animal object using the accessor (getter) methods.
        Be sure to include descriptive headings.
"""
# Test the Animal class here
print("*** Testing the Animal Class ***")



"""

*** Mammal Class (Subclass of Animal) ***
4. Define a class named Mammal. This class must be a subclass of the Animal class.
    a. Attributes:
        i. age
	b. Constructor - Create a constructor for the Mammal class that:
			i. Accepts values for gender, and age
			ii. Creates instance variables for speed and health using the "self." prefix.
			iii. Calls the constructor of the superclass (Animal class) passing in values for the
				gender instance variables.  This must be done so the constructor can
				create and set the gender which is inherited from the Animal class.

            ** Use the following code to call the constructor of the superclass **
				super(Mammal,self).__init__(gender)

    c. Methods:
        i. getAge()
        ii. setAge()
        v. move()
            -  Print "Mammal Moves" in this method.
        vi. makeNoise()
            - Print "Mammal Makes a Noise" in this method.

"""
# Define the Mammal class here


"""
* Testing the Mammal Class *
	1. Create an instance of Mammal passing in a "Female" for the gender and 4 for the age.
    2. Print the attributes of your mammal object using the accessor (getter) methods.
        Be sure to include descriptive headings.
    3. Modify the attribute values using the mutator (setter) methods.  Set the values to:
        - gender: "Male"
        - age: 5
    4. Again, print the attributes of your Animal object using the accessor (getter) methods.
        Be sure to include descriptive headings.
    5. Call the move() method.
    6. Call the makeNoise() method.
"""
# Test the Mammal class here
print("*** Testing the Animal Class ***")



"""

*** Feline class (Subclass of Mammal) ***
6. Define a class named Feline. This class must be a subclass of the Mammal class.
    a. Attributes:
        i. isIndoor
    b. Constructor:
        Create a constructor that accepts the gender, age, and isIndoor values and:
            -  Creates an instance variable for isIndoor.
            -  Calls the constructor of the superclass to set the gender and age:

            ** Use the following code to call the constructor of the superclass **
				super(Feline,self).__init__(gender, age)
    c. Methods:
        i. Getters and setters for the isIndoor property.
        ii. Create the makeNoise() method that:
            a. Prints "Feline says purr"
			b. Calls the makeNoise() method of the superclass (called method overriding).
			
			** Use the following code to override the makeNoise() 
				method of the Feline class and call the superclasses version instead. **

			super(Feline, self).makeNoise()
			
			

"""
# Define the Feline class here



"""
* Testing the Feline Class *
	1. Create an instance of Feline, passing in a "Male" for the gender, 2 for the age that
        lives indoors.
    2. Print all attributes of your feline object using the accessor (getter) methods.
        Be sure to include descriptive headings. Don't forget age and gender!!!
    3. Modify the attribute values using the mutator (setter) methods.  Set the values to:
        - gender: "Female"
        - age: 3
        - isIndoor: False
    4. Again, print the attributes of your Feline object using the accessor (getter) methods.
        Be sure to include descriptive headings. Don't forget age and gender!!!
    5. Call the makeNoise() method.



"""
# Test the Feline class here
print("*** Testing the Animal Class ***")







"""
*** Canine Class (Subclass of Mammal) ***
6. Define a class named Canine. This class must be a subclass of the Mammal class.
    a. Attributes:
        i. height
    b. Constructor:
        Create a constructor that accepts the gender, age, and height values and:
            -  Creates an instance variable for height.
            -  Calls the constructor of the superclass to set the gender and age:
    c. Methods:
        i. Getters and setters for the height property.
        ii. Create the makeNoise() method that:
            a. Prints "Canine says Howl"
            b. Calls the makeNoise() method of the superclass (called method overriding).	

"""
# Define the Canine class here




"""
* Testing the Canine Class *
	1. Create an instance of Canine, passing in a "Male" for the gender, 2 for the age
        with a height of 21.2 inches.
    2. Print all attributes of your canine object using the accessor (getter) methods.
        Be sure to include descriptive headings. Don't forget age and gender!!!
    3. Modify the attribute values using the mutator (setter) methods.  Set the values to:
        - gender: "Female"
        - age: 3
        - height: 12.98
    4. Again, print the attributes of your canine object using the accessor (getter) methods.
        Be sure to include descriptive headings. Don't forget age and gender!!!
    5. Call the makeNoise() method.


"""
# Test the Canine class here
print("*** Testing the Animal Class ***")

