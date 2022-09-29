def searching(filename,word):
    f=open(filename,'r')
    line_count=0
    word_Count=0
    for line in f.readlines():
        line_count+=1
        word_list=line.split(' ')
        word_Count=0
        for words in word_list:
            word_Count+=1
            if(word==words):
            
                return(line_count,word_Count)
    else:
        
        return None
    f.close()
    
    
    
    
    
result=searching('demo.txt','dell') 
print(result)       
            
        
        
    