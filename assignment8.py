#8. Define a function max() that takes two numbers as arguments and returns the largest of them.
def max(a, b):
   
    if a > b:
        return a
    else:
        return b
 
print ('Enter the first number')
n1= input()
 
print ('Enter the second number')
n2 = input()
 
print ('the larger number is' + str(max(n1,n2)))

'''OUTPUT:


Enter the first number  5
Enter the second number 6
the larger number is6
'''
