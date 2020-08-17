import pytest
import random
import string
import pytest

import session5
from session5 import time_it

from session5 import temp_converter
from session5 import polygon_area
from session5 import squared_power_list
from session5 import speed_converter
import os
import inspect
import re
import math
import random

README_CONTENT_CHECK_FOR = [
    'polygon_area_f',
    'temp_converter_f',
    'print_f',
    'squared_power_list_f',
    'speed_converter_f'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_time_it_repetition_zero_or_less():
    assert time_it(print, 1, 2, 3, sep='-', end=' ***\n',
                   repetitions=0) > 0, 'Check Time_it for repitition for zeor or less'


def test_time_it_print_function():
    assert time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitions=5) > 0, 'Check Time_it for print function'


def test_time_it_squared_power_list_function():
    assert time_it(squared_power_list, 2, start=0, end=5,
                   repetitions=5) > 0, 'Check Time_it for squared_power_list function'


def test_time_it_polygon_area_function():
    assert time_it(polygon_area, 15, sides=3, repetitions=10) > 0, 'Check Time_it for polygon_area_function'


def test_time_it_temp_converter_function():
    assert time_it(temp_converter, 100, temp_given_in='k',
                   repetitions=5) > 0, 'Check Time_it for temp_converter_function'


def test_time_it_speed_converter_function():
    assert time_it(speed_converter, 100, dist='mile', time='hr',
                   repetitions=5) > 0, 'Check Time_it for speed_converter_function'


####################

def test_print_function():
    output = print(1, 2, 3, sep='-', end='***\n')
    assert output == None, " Check print function"


def test_squared_power_list_function_output():
    number = random.randint(-100, 100)
    start = random.randint(0, 10)
    end = random.randint(start, 20)
    square_list = squared_power_list(number, start=start, end=end)
    squared_list_c = []
    for i in range(start, end + 1):
        squared_list_c.append(number ** i)
    assert square_list == squared_list_c, " Check squared power list function"


def test_squared_power_list_function_input_negative_power():
    number = random.randint(-100, 100)
    start = random.randint(-1000, 0)
    end = start + 5
    square_list = squared_power_list(number, start=start, end=end)
    squared_list_c = []
    assert square_list == squared_list_c, " Check squared power list function"


def test_squared_power_list_function_input_start_greater_than_end_():
    number = random.randint(-100, 100)
    start = random.randint(-1000, 0)
    end = start - 5
    square_list = squared_power_list(number, start=start, end=end)
    squared_list_c = []
    assert square_list == squared_list_c, " Check squared power list function"


def test_polygon_area_triangle():
    side_length = random.uniform(0, 10000)
    area = polygon_area(side_length, sides=3)
    assert math.isclose(area, (3 ** 0.5) / 4 * side_length ** 2), " Check your Polygon area function area of Triangle"


def test_polygon_area_function_square():
    side_length = random.uniform(0, 10000)
    area = polygon_area(side_length, sides=4)
    assert math.isclose(area, side_length ** 2), " Check your Polygon area function for square"


def test_polygon_area_function_pentagon():
    side_length = random.uniform(0, 10000)
    area = polygon_area(side_length, sides=5)
    assert math.isclose(area, 0.25 * side_length ** 2 * (5 * ((5 + 2 * (5) ** 0.5))) ** 0.5), "Check your Polygon area function for pentagon"


def test_polygon_area_function_area_hexagon():
    side_length = random.uniform(0, 10000)
    area = polygon_area(side_length, sides=6)
    assert math.isclose(area, 1.5 * (3 ** 0.5) * side_length ** 2), " Check your Polygon area function for hexagoan"


def test_polygon_area_function_negative_number_of_sides_input():
    side_length = random.uniform(0, 10000)
    area = polygon_area(side_length, sides=-1)
    assert area == None, " Check your Polygon area function for negative  input sides"


def test_polygon_area_function_negative_length_input():
    side_length = random.uniform(-10000, 0)
    side_length = random.uniform(-10000, 0)
    area = polygon_area(side_length, sides=3)
    assert area == None, " Check your Polygon area function for negative  input length"


def test_polygon_area_function_side_non_standard_input():
    side_length = random.uniform(0, 10000)
    sides = random.randint(7, 10000)
    area = polygon_area(side_length, sides=sides)
    assert area == None, " Check your Polygon area function for negative  input length"


def test_temp_converter_function_Kelvin_others():
    temp_k = random.uniform(0, 1000)
    (temp1, temp1_b, temp2, temp2_b) = temp_converter(temp_k, temp_given_in='k')
    temp1_c = temp_k - 273.15
    temp2_c = (temp_k - 273.15) * 9 / 5 + 32
    assert math.isclose(temp1, temp1_c) and math.isclose(temp2,
                                                         temp2_c), " Check temperature function for Kelvin convertion"


def test_temp_converter_function_Celius_others():
    temp_c = random.uniform(-273.15, 1000)
    (temp1, temp1_b, temp2, temp2_b) = temp_converter(temp_c, temp_given_in='c')
    temp1_c = temp_c * 9 / 5 + 32
    temp2_c = temp_c + 273.15
    assert math.isclose(temp1, temp1_c) and math.isclose(temp2,
                                                         temp2_c), " Check temperature function for Celius convertion"


def test_temp_converter_function_fahrenheit_others():
    temp_f = random.uniform(-459.67, 1000)
    (temp1, temp1_b, temp2, temp2_b) = temp_converter(temp_f, temp_given_in='f')
    temp1_c = (temp_f - 32) / 1.8
    temp2_c = (temp_f - 32) / 1.8 + 273.15
    assert math.isclose(temp1, temp1_c) and math.isclose(temp2,
                                                         temp2_c), " Check temperature function for fahrenheit convertion"


def test_temp_converter_function_less_than_min():
    temp_base = ('f', 'k', 'c')
    temp_base = random.choice(temp_base)
    min_temperature = {'f': -459.67, 'k': 0, 'c': -273.15}
    temp = min_temperature.get(temp_base) - 1
    (temp1, temp1_b, temp2, temp2_b) = temp_converter(temp, temp_given_in=temp_base)
    assert temp1 == None and temp2 == None, " Check temperature function for less than min values"


def test_temp_converter_function_non_standard_base():
    temp_base = ('J')
    (temp1, temp1_b, temp2, temp2_b) = temp_converter(100, temp_given_in=temp_base)
    assert temp1 == None and temp2 == None, " Check temperature function for less than min values"


def test_speed_converter_function_to_mph():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='mile', time='hr')
    speed_converted_c = speed * 0.621371
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to mph"


def test_speed_converter_function_to_meter_per_hour():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='m', time='hr')
    speed_converted_c = speed * 1000
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to meter/hr"


def test_speed_converter_function_to_ft_per_hour():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='ft', time='hr')
    speed_converted_c = speed * 3280.84
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to feet/hr"


def test_speed_converter_function_to_yrd_per_hour():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='yrd', time='hr')
    speed_converted_c = speed * 1093.61
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to yard/hr"


def test_speed_converter_function_to_mile_per_millisecond():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='mile', time='ms')
    speed_converted_c = speed * 0.621371 / (3600 * 10 ** 3)
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to mile/ms"


def test_speed_converter_function_to_km_per_millisecond():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='km', time='ms')
    speed_converted_c = speed / (3600 * 10 ** 3)
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to meter/ms"


def test_speed_converter_function_to_meter_per_millisecond():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='m', time='ms')
    speed_converted_c = speed * 1000 / (3600 * 10 ** 3)
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to meter/ms"


def test_speed_converter_function_to_ft_per_millisecond():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='ft', time='ms')
    speed_converted_c = speed * 3280.84 / (3600 * 10 ** 3)
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to feet/ms"


def test_speed_converter_function_to_yrd_per_millisecond():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='yrd', time='ms')
    speed_converted_c = speed * 1093.61 / (3600 * 10 ** 3)
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to yard/ms"


def test_speed_converter_function_to_mile_per_min():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='mile', time='min')
    speed_converted_c = speed * 0.621371 / 60
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to mile/min"


def test_speed_converter_function_to_km_per_min():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='km', time='min')
    speed_converted_c = speed / 60
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to meter/min"


def test_speed_converter_function_to_meter_per_min():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='m', time='min')
    speed_converted_c = speed * 1000 / 60
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to meter/min"


def test_speed_converter_function_to_ft_per_min():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='ft', time='min')
    speed_converted_c = speed * 3280.84 / 60
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to feet/min"


def test_speed_converter_function_to_yrd_per_min():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='yrd', time='min')
    speed_converted_c = speed * 1093.61 / 60
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to yard/min"


def test_speed_converter_function_to_mile_per_sec():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='mile', time='s')
    speed_converted_c = speed * 0.621371 / 3600
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to milesec"


def test_speed_converter_function_to_km_per_sec():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='km', time='s')
    speed_converted_c = speed / 3600
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to meter/sec"


def test_speed_converter_function_to_meter_per_sec():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='m', time='s')
    speed_converted_c = speed * 1000 / 3600
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to meter/sec"


def test_speed_converter_function_to_ft_per_sec():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='ft', time='s')
    speed_converted_c = speed * 3280.84 / 3600
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to feet/sec"


def test_speed_converter_function_to_yrd_per_sec():
    speed = random.uniform(0, 1000)
    speed_converted = speed_converter(speed, dist='yrd', time='s')
    speed_converted_c = speed * 1093.61 / 3600
    assert math.isclose(speed_converted, speed_converted_c), " Check Speed converter function from kmph to yard/sec"


def test_speed_converter_function_negative_speed():
    speed = random.uniform(-10000, -1)
    speed_converted = speed_converter(speed, dist='kmph', time='hr')
    assert speed_converted == None, " Check Speed converter function for negative input"


def test_speed_converter_function_undefined_dist_units():
    speed_converted = speed_converter(100, dist='ph', time='year')
    assert speed_converted == None, " Check Speed converter function for negative input"


def test_speed_converter_function_undefined_time_units():
    speed_converted = speed_converter(100, dist='ligh_year', time='day')
    assert speed_converted == None, " Check Speed converter function for negative input"

def test_undefined_function():
    undefined=0
    time_it(undefined, 100, dist='kmph', time='hr')
    assert time_it('undefined', 100, dist='kmph', time='hr')>0,"Check for Undefined function"