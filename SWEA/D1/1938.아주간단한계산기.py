
from traceback import print_tb


a, b = map(int, input().split())

plus=a+b
minus=a-b
mult=a*b
mod=a//b

print(plus,minus,mult,mod,sep="\n")