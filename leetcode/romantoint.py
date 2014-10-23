def romanToInt(s):
    s_dict={'X':10,'I':1,'V':5,'L':50,'M':1000,'C':100,'D':500}
    s_len=len(s)
    if(s_len==0):
        return 0
    if(s_len==1):
        return s_dict[s]
    x=0
    for i in range(s_len-1):
        if(s_dict[s[i]]<s_dict[s[i+1]]):
            x=x-s_dict[s[i]]
        else:
            x=x+s_dict[s[i]]
    x=x+s_dict[s[s_len-1]]
    return x
a="XX"
print romanToInt(a)