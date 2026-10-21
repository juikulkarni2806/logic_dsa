def countFreq(n):
    freq=[0]*10
    while(n!=0):
        last_digit=n%10
        freq[last_digit]+=1
        n//=10
    return freq

n=1345687965763
res=countFreq(n)

for i in range(len(res)):
    print(f" {i}->{res[i]}")