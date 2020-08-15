# Readme File for Assignment for Session 4 - Numeric Types II
### Created by Sriram Iyengar
## Session 4 - Numeric Types II
- Floats: Coercing to Integer
- Floats: Rounding
- Decimals
- Decimals: Constructors and Contexts
- Decimals: Math Operations
- Decimals: Performance Considerations
- Complex Numbers
- Booleans
- Booleans: Precedence and Short-Circuiting
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Class
### Qualean
    '''      
    Write a Qualean class that is inspired by Boolean+Quantum concepts. 
    We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1)
    but it internally picks an imaginary state. The moment you assign it a real number,
    it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with 
    it and stores that number internally after using Bankers rounding to 10th decimal place
    '''

### for  __and__ & __or__
  - This is not implemented as it is a `bitwise &` operation not the `logical and` operation and the base datatype is of `Decimal` class.
    A rejected PEP-335 (https://www.python.org/dev/peps/pep-0335/) does not allow the overloading of `logical and` operator.

### _/__repr__/_
- This method returns the representation of the Qualean object and the value it contains in a nicely formatted string.
### __str__
- This method returns the `str` object of value of the Qualean object mentioned.
### __add__
- This method overrides the basic implementation of `addition +` operator for the `Qualean` class. It also extends to `int` objects.
### __eq__
- This method overrides the equality checking `==` for the user defined `Qualean ` objects.
### __float__
- This method returns the float conversion of the `Qualean` object.
### __ge__
- This method overrides the greater than or equal to checking `>=` for the user defined `Qualean ` objects.
### __gt__
- This method overrides the greater than checking `>` for the user defined `Qualean ` objects.
### __invertsign__
- This method returns the opposite sign of value of the calling `Qualean` object.
### __le__
- This method overrides the lesser than or equal to checking `<=` for the user defined `Qualean ` objects.
### __lt__
- This method overrides the lesser than checking `<` for the user defined `Qualean ` objects.
### __mul__
- This method overrides the basic implementation of `multiplication *` operator for the `Qualean` class. It also extends to `int` objects.
### __sqrt__
- This method implements the mathematical Square root operation on the `Qualean` object. 
  It is implemented using `Context` class from the `decimal` module which contains the `sqrt` 
  functionality with precision of 10 decimal places and rounded using `decimal.ROUND_HALF_EVEN`.
### __bool__
-  This dunder method returns the `bool` value for the `Qualean` object.


## Functions used in Test File
### test_readme_exists 
- checks if Readme files exists

### test_readme_contents length 
- checks the content length of  Readme file
### test_readme_proper_description 
- checks the content length of  Readme file

### test_readme_file_for_formatting 
- checks the formatting of  Readme file

### test_indentations 
- checks if the Assignment code is properly formated

### test_function_name_had_cap_letter 
- checks if the Assignment code is function has capital letters

### test_function_100times_eq_100q 
- checks the sum of 100 Qualean values

### test_function_decimal_sqrt_check
- checks sqrt function is working  in assignment

### test_function_sum_million_q_eq_zero 
- checks if sum of 1 million values is near to zero in assignment

### test_function_q1_false_and_q2_not_defined 
- checks the short circuit in boolen function in assignment

### test_function_q1_True_or_q2_not_defined
- checks the short circuit in boolen function  in assignment

### test_function_Multiplication_mul 
- checks the multiplaction function

### test_function_invertsign 
- checks the invertion function in assignment
### test_function_float_conversion 
- checks the Qualean to float function in assignment

### test_function_greater 
- checks the greater than function in assignment

### test_function_greater_than_equal_to 
- checks the greater than and equal to  function in assignment

### test_function_lesser_than 
- checks the less than  function in assignment

### test_function_less_than_equal_to 
- checks the less than and equal to  function in assignment

### test_function_equality_true 
- checks the equlity function for True case in assignment

### test_function_equality_false 
- checks the equlity   function for false case in assignment

### test_function_qualean_bool 
- checks the less boolean  function in assignment

### test_function_valid_input 
- checks if the function checks for valid input in assignment

### test_function_invalid_integer_input 
- checks if the function for invalid input in assignment

### test_function_repr 
- checks repr function in assignment

### test_function_str 
- checks Str function in assignment

### test_function_add 
- checks addition  function in assignment

### test_function_bool 
- checks bool  function in assignment

***
> ![My Image](https://github.com/rsriramiyengar/EPAi-session4-rsriramiyengar/blob/master/images/Image01.JPG)
***

We are using python >3.8.3

The assignment is  tested by executing 'pytest' , from python shell in same folder
