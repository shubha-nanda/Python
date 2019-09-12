import math
import os
import random
import re
if __name__ == '__main__':
    s= input()
    result=solve(s)
    print(result)
def solve(s):
     s1 = s.split(" ")
     print(s1)
     return ' '.join([x.capitalize() for x in s1])