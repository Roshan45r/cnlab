data=input("Enter data:")
moddata=data+"0"*16
g = "10001000000100001"
limit = len(moddata)-len(g)+1
ans=""
div=moddata
for i in range(limit):
    if(div[0]=="1"):
        v=g
    else:
        v="0"*len(g)
    rem=""
    for j in range(len(g)):
        rem+=str(int(v[j])^int(div[j]))
    #print(rem)
    
    if(i<limit-1):
        div=rem[1:]+moddata[len(g)+i]
    if(i==limit-1):
        rem=rem[1:]
    ans=rem
        
print("Remainder : "+str(len(ans)))
print("Codeword : "+data+ans)
