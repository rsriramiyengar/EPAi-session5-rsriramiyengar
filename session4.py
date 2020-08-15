import random
import decimal
from decimal import Context
from decimal import Decimal
import cmath

global_ctx = Context(prec=10, rounding=decimal.ROUND_HALF_EVEN, clamp=1)
decimal.setcontext(global_ctx)


class Qualean:
    '''
        Write a Qualean class that is inspired by Boolean+Quantum concepts.
        We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1)
        but it internally picks an imaginary state. The moment you assign it a real number,
        it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with
        it and stores that number internally after using Bankers rounding to 10th decimal place
    '''

    def __init__(self, q):
        if (q != 0 and q != 1 and q != -1):
            raise ValueError('You can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1)')
        else:
            self.q = global_ctx.create_decimal_from_float(q * random.uniform(-1, 1))

    def __and__(self, other):
        """
        Not modified. As this funciton is for `bitwise` "and" operation
        not for the `logical` and operation.
        https://www.python.org/dev/peps/pep-0335/
        """
        pass

    def __or__(self, other):
        """
                Not modified. As this funciton is for `bitwise` "or" operation
                not for the `logical` "or" operation.
                https://www.python.org/dev/peps/pep-0335/
                """
        pass

    def __repr__(self):
        return 'Qualean={0}'.format(self.q)

    def __str__(self):
        return str(self.q)

    def __add__(self, other):
        if not isinstance(other, Qualean):
            return self.q + other
        else:
            return self.q + other.q

    def __eq__(self, other):
        if not isinstance(other, Qualean):
            return self.q == other
        return self.q == other.q

    def __float__(self):
        return float(self.q)

    def __ge__(self, other):
        if not isinstance(other, Qualean):
            return True
        return self.q >= other.q

    def __gt__(self, other):
        if not isinstance(other, Qualean):
            return True
        return self.q > other.q

    def __invertsign__(self):
        return -1 * self.q

    def __le__(self, other):
        if not isinstance(other, Qualean):
            return True
        else:
            raise self.q <= other.q

    def __lt__(self, other):
        if not isinstance(other, Qualean):
            return True
        else:
            raise self.q < other.q

    def __mul__(self, other):
        if not isinstance(other, Qualean):
            return global_ctx.multiply(self.q, other)
        return global_ctx.multiply(self.q, other.q)

    def __sqrt__(self):
        if self.q >= 0:
            return global_ctx.sqrt(self.q)
        else:
            return cmath.sqrt(self.q)

    def __bool__(self):
        try:
            return self.q != 0
        except NameError:
            return False
