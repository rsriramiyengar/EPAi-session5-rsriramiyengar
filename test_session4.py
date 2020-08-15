import pytest
import random
import string
import pytest

from  session4 import Qualean
import session4
import os
import inspect
import re
import math
import random
import decimal
from decimal import Decimal

states = [1, 0, -1]

README_CONTENT_CHECK_FOR = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
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
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_100times_eq_100q():
    q1 = Qualean(random.choice(states))
    new_q = Qualean(0)
    for _ in range(100):
        new_q += q1.q

    assert math.isclose(new_q, q1 * 100, rel_tol=1e-4)

def test_function_decimal_sqrt_check():
    q1 = Qualean(1)
    Decimal_Test=False
    print(Decimal_Test)
    if q1.q >= 0:
        with decimal.localcontext() as ctx:
            ctx.prec = 10
            ctx.rounding = decimal.ROUND_HALF_EVEN
            if  q1.__sqrt__() == Decimal(str(q1)).sqrt(context=ctx):
                Decimal_Test=True
                pass
            else:
                pass
    else:
        Decimal_Test= True
    print(Decimal_Test)
    assert Decimal_Test == True, "Check your the function"

def test_function_sum_million_q_eq_zero():
    q1 = 0
    TEST_million = True
    for x in range(100001):
        q = random.choice(states)
        q = Qualean(q)
        q1 = q1 + q.q
        print(q1)
    else:
        if  math.isclose(q1, 0):
            TEST_million=False
    assert TEST_million== True, 'Check'

def test_function_q1_false_and_q2_not_defined():
    q1 = Qualean(0)
    assert not bool(q1 and q2)

def test_function_q1_True_or_q2_not_defined():
    q1 = Qualean(1)
    assert bool(q1 or q2)

def test_function_Multiplication_mul():
    q1 = Qualean(random.choice(states))
    q2 = Qualean(0)
    assert q1 * q2 == 0

def test_function_invertsign():
    q1 = Qualean(random.choice(states))
    if q1 != 0:
        assert q1.__invertsign__() == -q1.q
    else:
        assert q1==0

def test_function_float_conversion():
    q1 = Qualean(random.choice(states))
    assert isinstance(q1.__float__(), float)

def test_function_greater():
    q1 = Qualean(random.choice(states))
    assert q1 + 1 > q1

def test_function_greater_than_equal_to():
    q1 = Qualean(random.choice(states))
    assert q1 + 1 >= q1

def test_function_lesser_than():
    q1 = Qualean(random.choice(states))
    assert q1 < q1 + 1

def test_function_less_than_equal_to():
    q1 = Qualean(random.choice(states))
    assert q1 <= q1 + 1

def test_function_equality_true():
    q1 = Qualean(random.choice(states))
    assert q1 == q1

def test_function_equality_false():
    q1 = Qualean(1)
    q2 = Qualean(0)
    assert not q1 == q2

def test_function_qualean_bool():
    q1 = Qualean(1)
    assert bool(q1)
    q1 = Qualean(0)
    assert not bool(q1)

def test_function_valid_input():
    q1 = Qualean(random.choice(states))
    assert isinstance(q1, Qualean)

def test_function_invalid_integer_input():
    with pytest.raises(ValueError) as execinfo:
        _ = Qualean(2)
    assert "ValueError" in str(execinfo)


def test_function_repr():
    assert "object at" not in Qualean(random.choice(states)).__repr__()


def test_function_str():
    assert "object at" not in Qualean(random.choice(states)).__str__()


def test_function_add():
    q1 = Qualean(random.choice(states))
    q2 = Qualean(random.choice(states))
    assert math.isclose(q1.__add__(q2), q1.q+q2.q, rel_tol=1e-8 )


def test_function_bool():
    q1 = Qualean(1)
    assert bool(q1)
    q1 = Qualean(0)
    assert not bool(q1)