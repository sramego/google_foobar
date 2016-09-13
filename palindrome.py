"""                                                                            
Palindrome                                                                     
==========                                                                     
To help Beta Rabbit crack the lock, write a function answer(n) which returns the
smallest positive integer base b, at least 2, in which the integer n is a      
palindrome. The input n will satisfy "0 <= n <= 1000".                         
Test cases                                                                     
==========                                                                     
Inputs:                                                                        
    (int) n = 0                                                                
Output:                                                                        
    (int) 2                                                                    
Inputs:                                                                        
    (int) n = 42                                                               
Output:                                                                        
    (int) 4                                                                    
Given a number n, return a base b where the number represented in that base is a palindrome.
                                                                               
"""                                                                            
#def answer(n):                                                                
for n in range(0,1001):                                                        
    if not (isinstance(n,int)):                                                
        break                                                                  
    for base in range(2,1000):                                                 
        temp = n                                                               
        ans = ''                                                               
        while(temp>=base):                                                     
            (d,m) = divmod(temp,base)                                          
            ans = str(m) + ans                                                 
            temp = d                                                           
            if(d<base):                                                        
                ans = str(d) + ans                                             
        #print ans                                                             
        if str(ans) == str(ans)[::-1]:                                         
            print "Number is %s Base is %s" % (n,base)                         
            break 
