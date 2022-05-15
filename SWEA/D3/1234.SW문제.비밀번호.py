for i in  range(10):
  numLen, numBer= input().split()
  idx=0
  numBer=list(numBer)
  while idx<len(numBer)-1:
    if (numBer[idx]==numBer[idx+1]):
      del numBer[idx:idx+2]
      idx-=1
    else:
      idx+=1
  
  print("#{} {}".format(i+1, "".join(numBer)))

  

