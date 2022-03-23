def my_function(a,b=0):
    
    print(a)
   
    
    result = a + b 
    
    return result 
    
    print(b)
    
#print( my_function(b=1, a =2) ) 

#ex1 cal abs values

def cal_abs(a):
    
    if type(a) is str:
        return ('wrong data type')
    
    elif a >=0:
        return a 
        
    else:
        return -a
        
print(cal_abs(-1))


#ex2

def cal_s(n,m):
    
    
    result = 0

    for i in range(n,m+1):
    
        result = result + i
    
    return result 


print(cal_s(1,6))

def cal_pie(n,m):
    
        
    result = 1 

    for i in range(n,m+1):
    
        result = result*i
    
    return result

print(cal_pie(1,6))

#ex3

def cal_f(m):
    
    if m == 0:
        return 1
    else:
        return m*cal_f(m-1)
        
print(cal_f(0))

def cal_p(n,m):
    
    return cal_f(m)/ cal_f(m-n)
    
print(cal_p(3,5))