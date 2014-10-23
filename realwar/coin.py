#@PydevCodeAnalysisIgnore
def get_sum(a,low,high):     # Assume this is the scale and costs O(1)
    return sum(a[low:high+1])

def find_couterfeit_coin(a,low,high):
    tmp_len=high-low+1
    if(tmp_len>5):           # divide the coins when n>5 
      if (tmp_len%2==1):     # when n is odd
        mid=low+tmp_len/2
        if(get_sum(a,low,mid-1)!=get_sum(a,mid+1,high)): #left part and right part are not balanced
           return max(find_couterfeit_coin(a,low,mid-1),find_couterfeit_coin(a,mid+1,high)) # counterfeit in one of them
        elif(a[low]==a[mid]):   # the counterfeit is not in the whole heap
            return -1
        else :
            return mid          # the mid is different one return it
      else:                  # when n is even
        mid=low+tmp_len/2
        if(get_sum(a, low, mid-1)==get_sum(a, mid, high)):  #left part and right part are balanced
            return -1
        else :
            return max(find_couterfeit_coin(a,low,mid-1),find_couterfeit_coin(a,mid,high)) # counterfeit in one of them
    else:
        if (tmp_len==3):   # when n<=5, we can find that coin in a stable way
            if(a[low]==a[low+1] and a[low]==a[high]): #not here
                return -1
            if(a[low]==a[high]):  # not low and high
                return low+1
            elif(a[low]==a[low+1]): # low or high
                return high
            else:
                return low
        if (tmp_len==4):
            if(a[low]==a[high]): # not low
                return find_couterfeit_coin(a, low+1, high)
            elif(a[low]==a[low+1]): #low or high
                return high
            else:
                return low
        if (tmp_len==5):
            if (a[low]==a[high]): #not low
                return find_couterfeit_coin(a, low+1, high)
            elif(a[low]==a[low+1]):  #low or high
                return high
            else:
                return low
#result index start form 1
def find_counterfeit(a):
    return find_couterfeit_coin(a, 0, len(a)-1)+1

a=[1,1,1,1,1,1,1,1,1,1,1,1,1,2]
print find_counterfeit(a)
b=[1,1,1,1,1,0,1]
print find_counterfeit(b)