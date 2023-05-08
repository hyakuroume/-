
import math
mean = (166.5 + 168.2 + 177.3 + 164.9 + 172.0 + 165.4 + 179.2 + 170.1) / 8

m = [166.5, 168.2, 177.3, 164.9, 172.0, 165.4, 179.2, 170.1]

wa = 0
for  i in range(8):
    wa +=  (m[i] - mean)**2


s = wa / len(m)

print(s)

s2 = math.sqrt(s)

print(s2)


