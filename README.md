# Readme File for Assignment for Session 5 - Functional Parameters
### Created by Sriram Iyengar
## Session 5 - Functional Parameters
- Arguments & Parameters; Positional and Keyword Arguments
- Unpacking
- Extending Unpacking
- *args
- Keyword arguments
- **kwargs
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## time_it function


### time_it('print', 1, 2, 3, sep='-', end= ' ***\n', repetitons=5)
### print_f
- This function prints the user given data for user provided  repetition number a user given input on screen with user given seperator and end variables for repetition
   and the avg run time per cycle.
- sep denotes the seperator to be used
- end denotes the end character  to be used
- repetitions defines the number of times it needs to be computed and printed.

### time_it('squared_power_list', 2, start=0, end=5, repetitions=5) #2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]
### squared_power_list_f
- This function computes and prints list of power of number for user input and the avg run time per cycle.
- Where 'start' specifies the start of power of number. Note start number cannot be less than zero and end number.
- Where 'end' specifies the end  of power of number.
- The step taken is one.
- repetitions defines the number of times it needs to be computed and printed. 

### time_it('polygon_area', 15, sides = 3, repetitons=10) # 15 is the side length. This polygon supports area calculations of upto a hexagon
### polygon_area_f
- This function computes and prints area of polygon for user input and the avg run time per cycle.
- '15' is the location where we define the +ve length of side.
- 'side' this defines the number(int) of sides the polygon which needs to be between 3 and 6.
- repetitions defines the number of times it needs to be computed and printed. 

## time_it('temp_converter', 100, temp_given_in = 'f', repetitons=100) # 100 is the base temperature given to be converted
### temp_converter_f
- This function computes and prints  Temperature from  user base units to others  and the avg run time per cycle.
- 'temp_given_in' is Input unit of temperature which can be  in 'k','c' or 'F') 
- '100' is the user defined temperature in user defined units. 
- repetitions defines the number of times it needs to be computed and printed.

### time_it('speed_converter', 100, dist='km', time='min', repetitons=200) #dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by user is in kmph
### speed_converter_f

- This function computes and prints  speed kmph to user selected units of distance & time and the avg run time per cycle.
- 'dist' is Input unit of distance which can be  in 'km' for kilometer, 'm' for meter, 'ft' for feet, 'yrd' for yard or 'mile' for mile.
- 'time' is Input unit of time which can be  in 'ms' for milli second , 's' for seconds, 'min' for minutes , 'hr'for hrs, ' day'for day}. 
- repetitions defines the number of times it needs to be computed and printed.

## Functions used in Test File
##def test_readme_exists():
- This test function check if readme files exists. 
### def test_readme_contents():
- This test function check if readme files has more than 500 words.
### def test_readme_proper_description():
- This test function check if readme files has described all the functions
### def test_readme_file_for_formatting():
- This test function checks if we have enough headers.
### def test_indentations():
- This test function checks if assignment file is properly indentation as per PEP8 guidelines
### def test_function_name_had_cap_letter():
- This test function checks if assignment file is functions don't have capital letters.
### def test_print_function():
- This test function checks special print functions is in order.
### def test_squared_power_list_function_output():
- This test function checks output of squared_power_list function.
### def test_squared_power_list_function_input_negative_power():
- This test function checks  squared_power_list function for negative power input.
### def test_squared_power_list_function_input_start_greater_than_end_():
- This test function checks  squared_power_list function for end value larger than start value.
### def test_polygon_area_triangle():
- This test function checks  polygon_area function for area of triangle.
### def test_polygon_area_function_square():
- This test function checks  polygon_area function for area of square.
### def test_polygon_area_function_pentagon():
- This test function checks  polygon_area function for area of pentagon.
### def test_polygon_area_function_area_hexagon():
- This test function checks  polygon_area function for area of hexagon.
### def test_polygon_area_function_negative_number_of_sides_input():
- This test function checks  polygon_area function for negative number of sides.(which is not possible.)
### def test_polygon_area_function_negative_length_input():
- This test function checks  polygon_area function for negative length of side.(which is not possible.)
### def test_polygon_area_function_side_non_standard_input():
- This test function checks  polygon_area function for number of sides other than 3 to 6.(which the function designed handle)
### def test_temp_converter_function_Kelvin_others():
- This test function checks  temp_converter function for Kelvin to Celius and fahrenheit.
### def test_temp_converter_function_Celius_others():
- This test function checks  temp_converter function for Celius to kelvin and fahrenheit.
### def test_temp_converter_function_fahrenheit_others():
- This test function checks  temp_converter function for fahrenheit to Celius and Kelvin.
### def test_temp_converter_function_less_than_min():
- This test function checks  temp_converter function for temperature less than allowable i.e {'f':-459.67,'k':0,'c':-273.15}
### def test_temp_converter_function_non_standard_base():
- This test function checks  temp_converter function for temperature base not defined without error or wrong results
## The following functions check for kmph to mile/hr,meter/hr, feet/hr & yard/hr
### - def test_speed_converter_function_to_mph():
### - def test_speed_converter_function_to_meter_per_hour():
### - def test_speed_converter_function_to_ft_per_hour():
### - def test_speed_converter_function_to_yrd_per_hour():
## The following functions check for kmph to mile/milli second,km/milli second,meter/milli second, feet/milli second & yard/milli second
### - def test_speed_converter_function_to_mile_per_millisecond():
### - def test_speed_converter_function_to_km_per_millisecond():
### - def test_speed_converter_function_to_meter_per_millisecond():
### - def test_speed_converter_function_to_ft_per_millisecond():
### - def test_speed_converter_function_to_yrd_per_millisecond():
## The following functions check for kmph to  mile/min,km/min,meter/min, feet/min & yard/min
### - def test_speed_converter_function_to_mile_per_min():
### - def test_speed_converter_function_to_km_per_min():
### - def test_speed_converter_function_to_meter_per_min():
### - def test_speed_converter_function_to_ft_per_min():
### - def test_speed_converter_function_to_yrd_per_min():
## The following functions check for kmph to mile/sec,km/sec,meter/sec, feet/sec & yard/sec
### - def test_speed_converter_function_to_mile_per_sec():
### - def test_speed_converter_function_to_km_per_sec():
### - def test_speed_converter_function_to_meter_per_sec():
### - def test_speed_converter_function_to_ft_per_sec():
### - def test_speed_converter_function_to_yrd_per_sec():
-----------------------------------------------------------------------------------------------
### def test_speed_converter_function_negative_speed():
- The following speed_converter_function for negative speed which is  physically not possible as it is scaler not vector.(Only Velocity can be negative)
### def test_speed_converter_function_undefined_dist_units():
- The following speed_converter_function for undefined distance unit without error or wrong results
### def test_speed_converter_function_undefined_time_units():
- The following speed_converter_function for undefined time unit without error or wrong results
### def test_undefined_function():
- The following check undefined function. which is yet to be developed.

***
> ![My Image](https://github.com/rsriramiyengar/EPAi-session5-rsriramiyengar/blob/master/images/Image01.JPG)
***

We are using python >3.8.3

The assignment is  tested by executing 'pytest' , from python shell in same folder
