import platform as p
print(p.system()) #Windows

import math
#*math.fabs(x):retorna el valor absoluto flotante de x
print(math.fabs(-12))   #12.0
#*abs(x):retorna el valor absoluto x
print(abs(-12))         #12
print(abs(-12.66))      #12.66


#*math.ceil(x):retorna el valor mayor proximo
print(math.ceil(3.01))         # 4
print(math.ceil(-3.01))        # -3
print(math.ceil(-3.99))        # -3


#*math.floor(x):retorna el valor menor proximo
print(math.floor(3.01))         # 3
print(math.floor(-3.01))        # -4
print(math.floor(-3.99))        # -4

#*math.trunc(x):retorna la parte entera
print(math.trunc(3.01))         # 3
print(math.trunc(-3.01))        # -3
print(math.trunc(-3.99))        # -3


#*math.fmod(x):retorna la parte entera
print(math.fmod(10, 5))        # 0.0
print(math.fmod(33, 5))        # 3.0
print(math.fmod(10, 3))        # 1.0


#*math.frexp(x):retorna la parte entera
print(math.frexp(12))        # (0.75, 4)
print(math.frexp(25))        # (0.78125, 5) -> 0.78125 * 2**5 -> 0.78125 * 32 = 25

print(math.sqrt(26))        #5.0990195135927845
print(math.isqrt(26))        #5
print(math.pow(2, 5))        #32.0


print(math.pi)              # 3.141592653589793
print(math.nan)             # nan
print(math.isnan(3))        # False
print(math.isnan(math.nan)) # True


