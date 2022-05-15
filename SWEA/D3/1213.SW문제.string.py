from re import S
from unittest import result


for i in range(10):
  problemNum=int(input())
  searchText=input()
  searchedText=input()

  resultNum=searchedText.count(searchText)

  print("#{} {}".format(problemNum,resultNum))
