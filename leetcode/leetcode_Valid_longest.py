#@PydevCodeAnalysisIgnore

def longestValidParentheses( s):
    tmp_len=len(s)
    if(tmp_len<=1):
        return 0
    tmp_broke=[]
    tmp_stack=[]
    max_r=0
    record=-1
    tmp_broke.append(-1)
    for i in range(tmp_len):
        if (s[i]=='('):
            tmp_stack.append(i)
            if(len(tmp_stack)==1):
                record=i
        else:
            if (len(tmp_stack)!=0):
                tmp_stack.pop()
            else:
                tmp_broke.append(i) 
    if(len(tmp_stack)!=0):
      tmp_stack.append(tmp_len)
      for j in range(len(tmp_stack)-1):
          tmp=tmp_stack[j+1]-tmp_stack[j]
          max_r=max(tmp,max_r)
      tmp_broke.append(record)
      for j in range(len(tmp_broke)-1):
         tmp=tmp_broke[j+1]-tmp_broke[j]
         max_r=max(tmp,max_r)  
    else:
        tmp_broke.append(tmp_len)
        for j in range(len(tmp_broke)-1):
          tmp=tmp_broke[j+1]-tmp_broke[j]
          max_r=max(tmp,max_r)  
          
    return (max_r-1)

a="())()("
print longestValidParentheses(a)