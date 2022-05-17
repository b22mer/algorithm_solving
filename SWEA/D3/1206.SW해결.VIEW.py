for i in range(10):
  numOfBuilding=int(input())
  buildingHeightList=list(map(int,input().split()))
  numOfFamily=0
  for j in range(2,numOfBuilding-2):
    if ((buildingHeightList[j] > buildingHeightList[j-1]) and (buildingHeightList[j] > buildingHeightList[j-2])) and ((buildingHeightList[j] > buildingHeightList[j+1]) and (buildingHeightList[j] > buildingHeightList[j+2])):
      sideBuildingHeight=max([buildingHeightList[j+1],buildingHeightList[j+2],buildingHeightList[j-1],buildingHeightList[j-2]])
      numOfFamily+=((buildingHeightList[j])-sideBuildingHeight)
  
  print("#{} {}".format(i+1,numOfFamily))
