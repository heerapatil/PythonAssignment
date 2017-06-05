#9. Define a function max_of_three() that takes three numbers as arguments and ret
def max(a, b,c):
   
    if (a > b)and( a>c):
        return a
    elif (b>c):
        return b
    else: return c
  
print ('Enter the first number')
n1= input()
 
print ('Enter the second number')
n2 = input()
print ('Enter the third number')
n3 = input()
 
print ('the larger number is' + str(max(n1,n2,n3)))
