def countFrequency(arr):
    freq=[0]*101
    for num in arr:
        freq[num-900]+=1
    return freq

arr=[901,901,902,906]
print(countFrequency(arr))