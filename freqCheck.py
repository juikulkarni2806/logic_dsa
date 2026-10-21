def FreqCheck(n,k):
    freq=[0]*10
    
    
    while(n!=0):
        last_digit=n%10
        freq[last_digit]+=1
        n//=10
    res=[]

    for i in range(len(freq)):
        if freq[i]>=k:
            res.append(i)
    return res

n=1236513312335411754
res=FreqCheck(n,3)

print(res)
# print(f"{i}->{res[i]}")