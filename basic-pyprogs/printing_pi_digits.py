from mpmath import mp

# # Set the precision
mp.dps = 10000000

# # Print pi to the desired precision
print(mp.pi)


'''from gmpy import mpfr
import gmpy

gmpy.get_context().precision = 10**7  # Set precision to 10 million digits

pi = mpfr('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
print(pi)'''
