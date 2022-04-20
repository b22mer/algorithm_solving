
test= input().split("_")
result=[]

for i in range(len(test)):
    result.append(test[i].upper())

print("_".join(result))
