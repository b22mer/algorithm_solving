N = int(input())

for i in range(N):

  if str(i+1).count("3")==0 and str(i+1).count("6")==0 and str(i+1).count("9")==0:
    print(i+1,end="")

  if str(i+1).count("3") != 0:

    for j in range(str(i+1).count("3")):
      print("-", end="")
    
  if str(i+1).count("6") != 0:

    for j in range(str(i+1).count("6")):
      print("-", end="")
    

  if str(i+1).count("9") != 0:

    for j in range(str(i+1).count("9")):
      print("-", end="")

  print(end=" ")
  


  
