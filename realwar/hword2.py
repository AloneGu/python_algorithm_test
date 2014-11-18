#@PydevCodeAnalysisIgnore
import bisect
def find_words(s,targets):
    my_dict={}
    result=[]
    for i in range(97,97+26):      #initial the dictionary 
      my_dict[chr(i)]=i-97
      result.append([])
    for i in range(len(s)):        #store the index of every character
        result[my_dict[s[i]]].append(i+1)
    final_result=[]
    for item in targets:        # for each target, find them in the dictionary, it runs k times
        final_result.append(find_word(result, item, my_dict))
    return final_result

def find_word(tmp,target,my_dict):  
    pos=0
    for i in range(len(target)):  # check every character in the dictionary, as described, at most 10 characters.
        tmp_list= tmp[my_dict[target[i]]]
        # the next character's index in the source string must be larger than the former's
        if(bisect.bisect_right(tmp_list,pos)==len(tmp_list)):  # costs O(logn)
            return "NO"
        pos=tmp_list[bisect.bisect_right(tmp_list,pos)]
    return "YES"

a="aabbccaa"
b=["abca","aaaa","cba","abab"]
print find_words(a,b)
c="algorithmisveryinteresting"
d=["love"]
print find_words(c,d)

