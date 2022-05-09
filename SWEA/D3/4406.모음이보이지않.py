testcase = int(input())

for i in range(testcase):
    testSentence=input()
    
    result=testSentence.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")

    print("#{} {}".format(i+1, result))
  


# replace는 데이터 값 자체를 변경시키고 저장하진 않고 잠깐만!