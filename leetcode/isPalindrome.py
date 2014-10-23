def isPalindrome(x):
        if(x<0 or x==10):
            return False
        if(x<10):
            return True
        div=10
        while(x/div>9):
            div=div*10
        while(x>10):
            a=x/div
            b=x%10
            if(a==b and x<100):
                return True
            if(a!=b):
                return False
            else:
                x=x-a*div
                x=x/10
                div=div/100
        if(x==0):
            return True
        elif(div==1):
            return True
        else:
            return False

print isPalindrome(9999)