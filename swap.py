arr=[10,20,30,40,50,60]
r=2
tempArr=[]
for i in range(r):
    tempArr.append(arr[i])

for i in range(0,len(arr)-r,1):
    arr[i]=arr[i+r]
    j=0
for i in range(len(arr)-r,len(arr),1):
    arr[i]=tempArr[j]
print(arr)