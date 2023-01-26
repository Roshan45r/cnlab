def division(code,pol):
    i=len(poly)
    temp=code[0:len(poly)]
    for j in range(0,len(code)-len(poly)):
        if(temp[0] != '0'):
            res=xor(temp,poly,len(poly))
            temp=res[1:]+code[i]
        else:
            temp=temp[1:]+code[i]
        i = i + 1
        print(temp)
    if(temp[0] != '0'):
            res=xor(temp,poly,len(poly))
            send = res[1:]
    else:
        send = temp[1:]
    return send
def xor(a, b, n):
    ans = ""
    for i in range(n):
        if (a[i] == b[i]):
            ans += "0"
        else:
            ans += "1"
    return ans
code = input("ENTER CODEWROD \n")
poly = "1101"
zeroes = "000"
modified_code = code+zeroes
sender = division(modified_code,poly)
receiver = code+sender
ans = division(receiver,poly)
if ans == "000":
    print("no error")
else:
    print("error data")
