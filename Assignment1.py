#1. Write a python script for creating directory,displaying its contents.
import os
os.mkdir("assignment")
os.chdir("assignment")
os.system("touch a.txt")
os.system("touch a11.txt")
print os.listdir(os.curdir)
print os.listdir('..')



'''
OUTPUT

python Assignment1.py['a.txt', 'a11.txt']
'''
