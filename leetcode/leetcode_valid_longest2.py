#@PydevCodeAnalysisIgnore
def find_max_len(s):
    if(len(s)<=1):
        return 0
    s_array=[]
    s_array.append(1)
    s_stack=[]
    for i in range(len(s)):
        if(s[i]=='('):
            s_stack.append(i+1)
            s_array.append(1)
        else:
            if(len(s_stack)==0):
                s_array.append(1)
            else:
                s_array.append(0)
                s_array[s_stack.pop()]=0
    s_array.append(1)
    start_pos=0
    s_max=-1
    for j in range(len(s)+2):
        if (s_array[j]==1):
            s_max=max(s_max,j-start_pos)
            start_pos=j
    return s_max-1

def find_max_len2(s):
    if(len(s)<=1):
        return 0
    s_stack=[]
    s_max=0
    for i in range(len(s)):
        if(s[i]=='('):
             s_stack.append(i)
        else:
            if(len(s_stack)!=0 and s[s_stack[len(s_stack)-1]]=='('):
                tmp=s_stack.pop()
                if (len(s_stack)!=0):
                   s_max=max(s_max,i-s_stack[len(s_stack)-1])
                else:
                   s_max=max(s_max,i+1) 
            else:
                s_stack.append(i)
        print s_stack
    return s_max 
a="(((())"
print find_max_len(a)