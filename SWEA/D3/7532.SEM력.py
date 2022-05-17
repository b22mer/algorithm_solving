T=int(input())
for i in range(T):
  S,E,M= map(int, input().split())
  chk=1
  results=0
  while True:
    Schk=chk%365
    Echk=chk%24
    Mchk=chk%29
    if Schk==0:
      Schk=365
    if Echk==0:
      Echk=24  
    if Mchk==0:
      Mchk=29
      
    if (S==Schk)and (E==Echk) and (M==Mchk):
      results=chk
      break
    chk+=1

  print("#{} {}".format(i+1, results))

