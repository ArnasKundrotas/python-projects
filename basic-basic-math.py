# just coding for the sake of it

print(4+5) # :))
print(4+5+1) # :))))

print(4-5+1) # :))))
print(4/5+1) # :))))
print(4*5+1) # :))))

# exponents
# law of exponents
# illustrating with latex

# the law of exponents --> adding exponents possible only when the base is the same
# 3**2 * 3**5 = 3**(2+5) = 3**7

print (3**2 * 3**5)
print (3**(2+5))

# fractional power sqrt etc.

print(3**(1/2))

import math
from IPython.display  import display, Math


print(display(Math('3^2\\times 3^4 = 3^{2+4}')))
# <IPython.core.display.Math object>
# None

x = 5
y = 5.1

print(display(Math('3^{3/4}\\times4^y=3933.09')))
print((x**(3/4)) * (4**y))

print(display(Math('\\frac{3^3}{x^y}=0.00735558')))
print((3**3)/(x**y))

print(display(Math('10^{x-4}=10')))
print(10**(x-4))


