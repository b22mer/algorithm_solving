A, B= map(int, input().split())

#가위 1 바위 2 보 3

if (A==1 and B==2):
  print("B")
elif (A==3 and B==1):
  print("B")
elif (A==2 and B==3):
  print("B")
else:
  print("A")

  