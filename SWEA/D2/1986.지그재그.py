# #
# n=int(input())


# sum=[]
# for i in range(n):
#   num=[]
#   z=int(input())
#   for j in range(z):


#     if j+1==z:
#       num.append(j+1)
#     elif ((j+1)%2!=0):
#       num.append(j+1)
#       num.append("-")
#     elif ((j+1)%3!=0):
#       num.append(j+1)
#       num.append("+")
#   sum.append(num)


# for i in range(n):
#   print("#",end="")
#   print(i+1, eval("".join(map(str,sum[i]))))



n = int(input())
result=[]
for i in range(n):
  sum=0
  s = int(input())

  for j in range(s):

    if ((j+1)%2!=0):
      sum+=j+1
    else:
      sum-=j+1
  result.append(sum)


for i in range(n):
  print("#",end="")
  print(i+1,result[i])

