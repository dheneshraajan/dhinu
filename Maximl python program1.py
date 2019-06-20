Total=256
def maximum_distinct_char(str, S): 
    cnt=[0]*Total   
    for i in range(S): 
        cnt[ord(str[i])] += 1  
    maximum_distinct = 0
    for i in range(Total): 
        if (cnt[i] != 0): 
            maximum_distinct += 1    
    return maximum_distinct 
def smlSubStr_maxDistictChar(str): 
    S=len(str)
    max_distinct = maximum_distinct_char(str, S) 
    minsub=S     
    for i in range(S): 
        for j in range(S): 
            subs=str[i:j] 
            subs_length=len(subs) 
            sub_distinct_char=maximum_distinct_char(subs,subs_length) 
              
            if (subs_length<minsub and 
                max_distinct==sub_distinct_char): 
                minsub=subs_length 
    return minsub 
if __name__=="__main__":    
    str =input()    
    answer=smlSubStr_maxDistictChar(str); 
    print(answer)
