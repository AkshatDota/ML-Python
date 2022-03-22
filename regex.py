import re

#  Add [] around words starting with s and containing e and t in any order.

ip = 'oreo not a _a2_ roar took 22'
print(re.sub(r'\b(\w|(\w)\w*\2)\b', 'X', ip))