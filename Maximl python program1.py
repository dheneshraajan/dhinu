
NO_OF_CHARS=256
def maximum_distinct_char(str, n): 
    count=[0]*NO_OF_CHARS   
    for i in range(n): 
        count[ord(str[i])] += 1  
    maximum_distinct = 0
    for i in range(NO_OF_CHARS): 
        if (count[i] != 0): 
            maximum_distinct += 1    
    return maximum_distinct 
def smallesteSubstr_maxDistictChar(str): 
    n = len(str)
    max_distinct = maximum_distinct_char(str, n) 
    minsub= n      
    for i in range(n): 
        for j in range(n): 
            subs=str[i:j] 
            subs_length=len(subs) 
            sub_distinct_char=maximum_distinct_char(subs,subs_length) 
              
            if (subs_length < minsub and 
                max_distinct == sub_distinct_char): 
                minsub=subs_length 
    return minsub 
if __name__=="__main__":    
    str =input()    
    answer=smallesteSubstr_maxDistictChar(str); 
    print(answer)
