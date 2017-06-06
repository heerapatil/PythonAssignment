# Question4 :Write a Python program to count the number of lines in a text file

import io
fo=open("file.txt","w+")
fo.write("hi\nhello\nhow r u")
fo.close()
filename="file.txt"
myfile = open(filename)
lines= len(myfile.readlines())
print "There are%d lines in %s "%(lines,filename)


'''OUTPUT:There are3 lines in file.txt 
'''
