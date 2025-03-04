import decimal
from decimal import Decimal

from mpmath import mp

from upow.constants import SMALLEST
from upow.helpers import round_up_decimal, round_up_decimal_new

# Set precision (optional)
mp.dps = 500  # Set precision to 50 digits

# Perform division
result = mp.fdiv(10, 3.4055950505, dps=50, )

mp.pretty = False

print(result)
print(type(result))
print(len(str(result)))
# print(Decimal(result))

decimal.getcontext().prec = 500
re = Decimal(10) / Decimal(3.4055950505)
print((re))


# dec = Decimal(24)
# print((dec * SMALLEST) % 1)
# print((dec * SMALLEST) % 1 != 0.0)
# print(round_up_decimal(dec))
# print(round_up_decimal_new(dec))
# if (decimal * SMALLEST) % 1 != 0.0:
